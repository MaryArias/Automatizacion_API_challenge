# pages/import_api.py
from loguru import logger
import requests

class PersonAPI:
    def __init__(self, base_url, token="xxx"):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def import_person(self, person_id):
        body = [{"personId": person_id}]
        logger.info(f"Enviando POST a: {self.base_url}")
        logger.debug(f"Headers: {self.headers}")
        logger.debug(f"Body: {body}")
        try:
            response = requests.post(self.base_url, json=body, headers=self.headers)
            logger.success(f"Status Code: {response.status_code}")
            logger.debug(f"Response Body: {response.json()}")
            return response
        except requests.RequestException as e:
            logger.error(f"Error en la request: {e}")
            return None

    def import_person_sin_id(self):
        from loguru import logger
        import requests

        body = [{}] 
        logger.info(f"Enviando POST sin personId a: {self.base_url}")
        try:
            response = requests.post(self.base_url, json=body, headers=self.headers)
            logger.success(f"Status Code: {response.status_code}")
            logger.debug(f"Response Body: {response.json()}")
            return response
        except requests.RequestException as e:
            logger.error(f"Error en la request: {e}")
            return None

