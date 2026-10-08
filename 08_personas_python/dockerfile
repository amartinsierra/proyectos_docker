FROM ubuntu:24.04

RUN apt-get update && apt-get install -y python3 && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY personas.py .

RUN useradd --create-home appuser && mkdir /datos && chown -R appuser:appuser /app /datos

USER appuser

VOLUME /datos

ENTRYPOINT ["python3", "personas.py"]