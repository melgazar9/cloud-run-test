FROM amd64/python:3.10.12-slim-buster

ARG CI=true

RUN env

ENV PATH="/root/.local/bin:$PATH"
ENV APP_HOME=/app
ENV PYTHONUNBUFFERED=1
WORKDIR $APP_HOME
COPY . $APP_HOME

RUN apt-get update && rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN pip install -U pip && pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "host.py"]
