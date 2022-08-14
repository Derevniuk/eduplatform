FROM python:3
#ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN pip install -U pip && \
   pip install poetry && \
   poetry config virtualenvs.create false && \
   poetry install

COPY . /code/
EXPOSE 8080
