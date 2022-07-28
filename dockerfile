FROM python:3-slim as python
ENV PYTHONUNBUFFERED=true
WORKDIR /app/backend


FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
COPY . ./
RUN pip install --user poetry



FROM python as runtime
ENV PATH="/app/backend. venv/bin:$PATH"
COPY --from=poetry /app/backend /app/backend
EXPOSE 8000