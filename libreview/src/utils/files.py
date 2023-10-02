import requests

from datetime import datetime

from src import settings


def download_file_from_s3(patient_id, s3_url):
        response = requests.get(s3_url)
        content = response.content

        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{patient_id}_{date}.csv"

        with open(f"{settings.MEDIA_FILES_DIR}/{file_name}", "wb") as f:
            f.write(content)
            f.close()

        return content
