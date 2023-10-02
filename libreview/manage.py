from src.services.libreview_api import LibreViewAPI
from src import settings


if __name__ == "__main__":
    api = LibreViewAPI()
    patient_ids = [settings.DEFAULT_PATIENT_ID]
    api.export_glucose_history(patient_ids)
