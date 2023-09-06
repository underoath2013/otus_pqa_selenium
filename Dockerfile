FROM python:3.11-alpine

WORKDIR /opencart

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY /tests ./tests
COPY /page_objects ./page_objects
COPY conftest.py .
COPY pytest.ini .


CMD ["pytest", \
    "--browser", "chrome", \
    "--url", "http://192.168.0.103:8081", \
    "--maximize", \
    "--log_level", "INFO", \
    "--bv", "116" \
]
