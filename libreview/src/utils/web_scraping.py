from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from src import settings


def login():
    api_token = None

    browser = Chrome()

    browser.get(settings.LOGIN_URL)
    browser.find_element(By.ID, "loginForm-email-input").send_keys(settings.LOGIN_EMAIL)
    browser.find_element(By.ID, "loginForm-password-input").send_keys(settings.LOGIN_PASSWORD)
    browser.find_element(By.ID, "loginForm-submit-button").click()

    browser.get(settings.LOGIN_SEND_CODE_URL)
    browser.find_element(By.ID, "twoFactor-step1-next-button").click()

    soup = BeautifulSoup(browser.page_source, "html.parser")

    return api_token
