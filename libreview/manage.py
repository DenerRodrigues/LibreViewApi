from src.services.libreview_api import LibreViewAPI
from src.utils.web_scraping import LibreViewWebScraping
from src import settings


if __name__ == "__main__":
    api_key = settings.API_KEY

    if settings.LOGIN_WEB_SCRAPING and not api_key:
        web_scraping = LibreViewWebScraping()
        api_key = web_scraping.login()
        web_scraping.browser.close()

    api = LibreViewAPI(api_key)

    if settings.DEFAULT_PATIENT_ID:
        patient_ids = [settings.DEFAULT_PATIENT_ID]
    else:
        patient_ids = [patient.get("id") for patient in api.get_patients()]
    
    api.export_glucose_history(patient_ids)
