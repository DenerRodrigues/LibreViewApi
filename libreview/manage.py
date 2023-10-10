from src.services.libreview_api import LibreViewAPI
from src.utils import web_scraping
from src import settings


if __name__ == "__main__":
    api_key = settings.API_KEY
    api = LibreViewAPI(api_key)

    if not api_key:
        api_key = web_scraping.login()
        api.validate_verification_code(api_key)

    if settings.DEFAULT_PATIENT_ID:
        patient_ids = [settings.DEFAULT_PATIENT_ID]
    else:
        patient_ids = [patient.get("id") for patient in api.get_patients()]
    
    api.export_glucose_history(patient_ids)
