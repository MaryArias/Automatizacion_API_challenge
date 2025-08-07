# tests/test_import.py
import pytest
from pages.import_api import PersonAPI
from db.validators import validation_persona_en_db
from loguru import logger

@pytest.fixture
def api(base_url):
    return PersonAPI(base_url)

@pytest.mark.parametrize("person_id", [111])
def test_happy_path(api, person_id):
    response = api.import_person(person_id)
    assert response is not None
    assert response.status_code == 200
    assert "status" in response.json()
    db_result = validation_persona_en_db(person_id)
    assert db_result is not None, f"personId {person_id} no se encontró en la base de datos"
    logger.info(f"Datos en la base para personId {person_id}: {db_result}")

@pytest.mark.parametrize("person_id", ["", None, -1])
def test_sad_path(api, person_id):
    response = api.import_person(person_id)
    assert response is not None
    assert response.status_code != 200

def test_sad_path_sin_person_id(api):
    response = api.import_person_sin_id()
    assert response is not None
    assert response.status_code != 200
