FROM python:3.8-slim

# Project setup

ENV VIRTUAL_ENV=/opt/venv

RUN apt-get update && apt-get clean

RUN python -m venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --quiet --upgrade pip && \
    pip install --quiet pip-tools
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./compose/app/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./compose/app/celery/worker/start.sh /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/app/celery/beat/start.sh /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/app/celery/flower/start.sh /start-flower
RUN chmod +x /start-flower

WORKDIR /app

COPY ./app/nltk_pkg.py /app/nltk_pkg.py
RUN python /app/nltk_pkg.py
