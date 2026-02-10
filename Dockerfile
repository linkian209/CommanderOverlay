FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p instance

ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--worker-class", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "--workers", "1", "app:create_app()"]
