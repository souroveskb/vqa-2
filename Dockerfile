FROM python:3.10-buster as builder

ENV PATH="/root/.local/bin:$PATH" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN python -m pip install --user pipx \
    && pipx ensurepath \
    && pipx install poetry==1.8.2

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root -vvv

FROM python:3.10-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    SERVER_PORT=${SERVER_PORT} 

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY . .

EXPOSE ${SERVER_PORT}

# CMD ["sh", "-c", "python -m uvicorn server:app --host 0.0.0.0 --port ${SERVER_PORT}"]
# CMD ["sh", "-c", "python config_gen.py ; streamlit run frontend.py --server.port=${FRONTEND_PORT} --server.address=0.0.0.0"]
CMD ["streamlit run frontend.py --server.port=${SERVER_PORT} --server.address=0.0.0.0"]