FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry

COPY . /app

RUN poetry install


CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]