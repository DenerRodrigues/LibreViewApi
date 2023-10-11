# LibreViewApi
[Python](https://www.python.org) Library for the [LibreView](https://www.libreview.com/) application


Quickstart
----------

#### Clone repository
```shell
git clone https://github.com/DenerRodrigues/libreview-lib.git
```

#### Install requirements.txt

```shell
pip install -r requirements.txt
```

#### Set environment variables in the `.env` file at project root

Variable                                 | Description                                | Example
-----------------------------|------------------------------------------------------- |-------------------------------------------------------
ANTI_CAPTCHA_KEY             | DEFINES ANTICAPTCHAOFFICIAL KEY                        | 0Dec18039db5bc8gd04a02c4269cdg76
CAPTCHA_WEBSITE_URL          | DEFINES LIBREVIEW URL                                  | https://www.libreview.com
CAPTCHA_WEBSITE_KEY          | DEFINES LIBREVIEW CAPTCHA KEY                          | 6LdiiXQUAAAAANKvWs9y2SNd45_PvqYg5vWjDq6r
API_KEY                      | DEFINES LIBREVIEW API KEY (OPTIONAL)                   | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
API_URL                      | DEFINES LIBREVIEW API URL                              | https://api.libreview.io
LOGIN_WEB_SCRAPING           | DEFINES WHETHER LOGIN WILL BE BY WEB SCRAPING (0/1)    | 1
LOGIN_URL                    | DEFINES LOGIN URL                                      | https://www.libreview.com
LOGIN_COUNTRY_LANGUAGE_URL   | DEFINES COUNTRY LANGUAGE URL                           | https://www.libreview.com/chooseCountryLanguage
LOGIN_SEND_CODE_URL          | DEFINES SEND CODE URL                                  | https://www.libreview.com/auth/finishlogin
LOGIN_EMAIL                  | DEFINES EMAIL TO LOGIN                                 | user@gmail.com
LOGIN_PASSWORD               | DEFINES PASSWORD TO LOGIN                              | 123456
DEFAULT_PATIENT_ID           | DEFINES DEFAULT PATIENT ID (OPTIONAL)                  | f2500322-c59a-11ec-8b95-0242ac110003


#### Create a `media` folder
```shell
mkdir libreview/src/media
```

#### Generate a gmail_token.json
You must generate a `gmail_token.json` from your Google Account and save it in the `media` folder


#### Run Application
```shell
python libreview/manage.py
```

