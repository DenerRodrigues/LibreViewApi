from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

from src import settings


def solve_recaptcha():
    solver = recaptchaV2Proxyless()

    solver.set_verbose(1)
    solver.set_key(settings.ANTI_CAPTCHA_KEY)
    solver.set_website_url(settings.CAPTCHA_WEBSITE_URL)
    solver.set_website_key(settings.CAPTCHA_WEBSITE_KEY)

    captcha_response = solver.solve_and_return_solution()
    return captcha_response
