# conftest.py
import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://api.test.worldsys.ar/import"
