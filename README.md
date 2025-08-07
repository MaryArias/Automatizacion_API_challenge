
# Challenge Técnico - Automatización de API

Este proyecto resuelve un challenge técnico de automatización de pruebas sobre una API REST utilizando **Python**, **Pytest** y el patrón **POM (Page Object Model)** adaptado a testing de APIs.

Incluye:
- Casos Happy Path y Sad Path
- Logs detallados con Loguru
- Validación dinámica del campo `personId`
- Validación opcional contra una base de datos
- Soporte para pruebas BDD con Behave

---

## Tecnologías usadas

- Python 3.x
- [Pytest](https://docs.pytest.org/)
- [Requests](https://docs.python-requests.org/)
- [Loguru](https://github.com/Delgan/loguru)
- [Behave (opcional)](https://behave.readthedocs.io/)
- SQLite (o base de datos compatible para validación)

---
### Estructura del proyecto:

```bash
AUTOMATIZACIÓN_DE_API/
├── db/
│   └── validators.py
├── pages/                # POM para la API
│   └── import_api.py
├── tests/                # Pruebas con Pytest
│   ├── test_import.py
│   └── import_steps.py
├── environment.py
├── conftest.py
├── requirements.txt
└── README.md
```
---

## Instalación
## Crear y activar un entorno virtual:
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

## Instalar las dependencias: 
pip install -r requirements.txt

## Ejecución de los tests: 
pytest tests/test_import.py -v


## Extras implementados
Logs con loguru
Separación clara de lógica y tests
Casos negativos bien definidos
Escenarios BDD con Behave (opcional)

## Autora

Desarrollo como parte de un challenge técnico de QA Automation. 

Arias Marianella 
