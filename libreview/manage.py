from src.services.libreview_api import LibreViewAPI
from src import settings


if __name__ == "__main__":
    api = LibreViewAPI()

    if settings.DEFAULT_PATIENT_ID:
        patient_ids = [settings.DEFAULT_PATIENT_ID]
    else:
        patient_ids = [patient.get("id") for patient in api.get_patients()]
    
    api.export_glucose_history(patient_ids)
