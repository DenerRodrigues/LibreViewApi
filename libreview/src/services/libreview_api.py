import pprint
import requests
import time

from src import settings
from src.services.gmail_api import GmailAPI
from src.utils.files import download_file_from_s3
from src.utils.recaptcha import solve_recaptcha


class LibreViewAPI:
    def __init__(self, api_key=None):
        self.api_url = settings.API_URL
        self.__api_key = api_key or self.login()

    def login(self):
        print("login")

        url = f"{self.api_url}/auth/login"

        data = {
            "email": settings.LOGIN_EMAIL,
            "password": settings.LOGIN_PASSWORD,
        }

        response = requests.post(url, json=data)
        json_response = response.json()

        api_key = json_response.get("data", {}).get("authTicket", {}).get("token")
        print(api_key)

        self.send_verification_code_to_email(api_key)
        result = self.validate_verification_code(api_key)

        self.__api_key = result.get("authTicket", {}).get("token")

        return result

    def send_verification_code_to_email(self, api_key):
        print("send code to email")

        url = f"{self.api_url}/auth/continue/2fa/sendcode"
        headers = {
            "Authorization": f"Bearer {api_key}",
        }

        data = {"isPrimaryMethod": "true"}

        response = requests.post(url, json=data, headers=headers)
        json_response = response.json()
        pprint.pprint(json_response)
        return json_response

    def validate_verification_code(self, api_key):
        print("validate verification code")

        url = f"{self.api_url}/auth/continue/2fa/result"
        headers = {"Authorization": f"Bearer {api_key}"}

        data = {
            "code": GmailAPI().get_verification_code(),
            "isPrimaryMethod": True,
        }

        response = requests.post(url, json=data, headers=headers)
        json_response = response.json()
        pprint.pprint(json_response)
        return json_response.get("data")

    def dashboard(self):
        print("post dashboard")

        url = f"{self.api_url}/dashboard"

        headers = {"Authorization": f"Bearer {self.__api_key}"}

        data = {
            "columns": [
                "firstName",
                "lastName",
                "email",
                "dob",
                "lastAvailableData",
                "avgGlucose",
                "sensorDailyScans",
                "percentGlucoseInTarget",
                "libreViewStatus",
            ],
            "filters": [],
            "interval": 14,
            "view": "Dashboard.allPatients",
            "count": 100,
            "page": 1,
            "searching": {},
            "sort": {"desc": False, "key": "firstName"},
        }

        response = requests.post(url, json=data, headers=headers)
        json_response = response.json()
        pprint.pprint(json_response.get("data"))
        return json_response.get("data")

    def get_patients(self):
        print("get patients")

        dashboard = self.dashboard()
        return dashboard.get("results")

    def get_glucose_history(self, patient_id, num_periods: int = 1, period: int = 1):
        print("get glucose history")

        url = f"{self.api_url}/patients/{patient_id}/glucoseHistory"

        headers = {"Authorization": f"Bearer {self.__api_key}"}

        params = {
            "numPeriods": num_periods,
            "period": period,
        }

        response = requests.get(url, params=params, headers=headers)
        json_response = response.json()
        pprint.pprint(json_response.get("data"))
        return json_response.get("data")

    def get_s3_url(self, poll_channel_url):
        headers = {"Authorization": f"Bearer {self.__api_key}"}

        response = requests.get(poll_channel_url, headers=headers)
        json_response = response.json()
        poll_url = json_response.get("data", {}).get("ws")

        s3_url = None

        while not s3_url:
            response = requests.get(poll_url, headers=headers)
            json_response = response.json()
            pprint.pprint(json_response)

            s3_url = json_response.get("args", {}).get("url")
            if s3_url:
                break
            else:
                time.sleep(5)

        return s3_url

    def export_glucose_history(self, patient_ids):
        print("export")

        for patient_id in patient_ids:
            try:
                captcha_response = solve_recaptcha()
            except Exception as e:
                pprint.pprint(e)
                return

            url = f"{self.api_url}/patients/{patient_id}/export"

            headers = {"Authorization": f"Bearer {self.__api_key}"}

            data = {"type": "glucose", "captchaResponse": captcha_response}

            response = requests.post(url, json=data, headers=headers)
            json_response = response.json()
            pprint.pprint(json_response)

            poll_channel_url = json_response.get("data").get("url")
            s3_url = self.get_s3_url(poll_channel_url)

            download_file_from_s3(patient_id, s3_url)
