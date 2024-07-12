FROM python:3.10-bullseye as builder

RUN pip install poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --no-interaction --no-ansi

FROM python:3.10-slim-bullseye

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app/src:$PYTHONPATH

WORKDIR /app

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY HW2/src /app/HW2/src

CMD ["uvicorn", "HW2.src.main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000