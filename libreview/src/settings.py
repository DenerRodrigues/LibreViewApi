import os

from dotenv import load_dotenv


load_dotenv()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_FILES_DIR = os.getenv("MEDIA_FILES_DIR", f"{BASE_DIR}/media")

ANTI_CAPTCHA_KEY = os.getenv("ANTI_CAPTCHA_KEY")
CAPTCHA_WEBSITE_URL = os.getenv("CAPTCHA_WEBSITE_URL")
CAPTCHA_WEBSITE_KEY = os.getenv("CAPTCHA_WEBSITE_KEY")

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_SEND_CODE_URL = os.getenv("LOGIN_SEND_CODE_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

DEFAULT_PATIENT_ID = os.getenv("DEFAULT_PATIENT_ID")
