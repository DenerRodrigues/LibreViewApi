from bs4 import BeautifulSoup
from selenium.webdriver import Firefox

from src import settings


def login():
    api_token = None

    browser = Firefox()

    browser.get(settings.LOGIN_URL)
    browser.find_element_by_id("loginForm-email-input").send_keys(settings.LOGIN_EMAIL)
    browser.find_element_by_id("loginForm-password-input").send_keys(settings.LOGIN_PASSWORD)
    browser.find_element_by_id("loginForm-submit-button").click()

    browser.get(settings.LOGIN_SEND_CODE_URL)
    browser.find_element_by_id("twoFactor-step1-next-button").click()

    soup = BeautifulSoup(browser.page_source, "html.parser")

    return api_token
