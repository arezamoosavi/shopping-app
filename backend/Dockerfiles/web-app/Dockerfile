FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies required for psycopg2 python package
RUN apk update && apk add libpq
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk update && apk add libffi-dev

RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
RUN pip install --no-cache-dir psycopg2-binary
RUN pip install --no-cache-dir gunicorn daphne

RUN mkdir -p /src

RUN addgroup -S django \
    && adduser -S -G django django

COPY ./Dockerfiles/web-app/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /src
COPY ./run_web.sh /run_web.sh
RUN chmod +x /run_web.sh

ENTRYPOINT ["/entrypoint.sh"]

# ENV name John Dow
# ENTRYPOINT echo "Hello, $name"
# ENTRYPOINT ["/bin/bash", "-c", "echo Hello, $name"]

