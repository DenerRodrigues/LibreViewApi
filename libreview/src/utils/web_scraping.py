import json
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from src import settings
from src.services.gmail_api import GmailAPI


class LivreViewWebScraping:
    def __init__(self):
        self.browser = Chrome()

    def _find_element_by_id(self, element_id, clear=False, max_trying=5):
        trying = 0
        element = None

        while not element:
            try:
                element = self.browser.find_element(By.ID, element_id)
                if clear:
                    time.sleep(1)
                    element.clear()
            except:
                time.sleep(1)
                trying += 1
                if trying == max_trying:
                    raise

        return element

    def _get_api_key(self):
        session_storage = self.browser.execute_script("return sessionStorage;")
        return json.loads(session_storage.get("token", {})).get("token")

    def login(self):
        api_key = None

        self.browser.get(settings.LOGIN_URL)

        self.select_country()

        self._find_element_by_id("loginForm-email-input").send_keys(settings.LOGIN_EMAIL)
        self._find_element_by_id("loginForm-password-input").send_keys(settings.LOGIN_PASSWORD)
        submit_button = self._find_element_by_id("loginForm-submit-button")
        self.browser.execute_script("arguments[0].click();", submit_button)

        self.send_code_verification()
        self.validate_verification_code()
        self.check_code_error()

        api_key = self._get_api_key()

        return api_key

    def select_country(self):
        self._find_element_by_id("country-select").send_keys("BR")

        submit_button = self._find_element_by_id("submit-button")
        self.browser.execute_script("arguments[0].click();", submit_button)

    def send_code_verification(self):
        next_button = self._find_element_by_id("twoFactor-step1-next-button")
        self.browser.execute_script("arguments[0].click();", next_button)

    def validate_verification_code(self):
        code_input = self._find_element_by_id("twoFactor-step2-code-input", clear=True)

        code = GmailAPI().get_verification_code()
        
        code_input.send_keys(code)
        time.sleep(1)

        next_button = self._find_element_by_id("twoFactor-step2-next-button")
        self.browser.execute_script("arguments[0].click();", next_button)

    def check_code_error(self, resend_code=True):
        try:
            code_error = self._find_element_by_id("twoFactor-step2-code-input-error-text", max_trying=2)
        except:
            code_error = False

        if code_error and resend_code:
            self.resend_code()
            self.validate_verification_code()

    def resend_code(self):
        resend_button = self._find_element_by_id("twoFactor-step2-resend-button")
        self.browser.execute_script("arguments[0].click();", resend_button)
