FROM python:3.6.5-alpine3.7 AS builder

ENV PATH=$PATH:/root/.local/bin
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /usr/src/app/

RUN apk add --no-cache --virtual .build-deps \
        build-base \
        linux-headers \
        openssl-dev \
        zlib-dev

COPY requirements.txt .

RUN pip install --user -r requirements.txt && \
    find $(python -m site --user-base) -type f -name "*.pyc" -delete && \
    find $(python -m site --user-base) -type f -name "*.pyo" -delete && \
    find $(python -m site --user-base) -type d -name "__pycache__" -delete && \
    find $(python -m site --user-base) -type d -name "tests" -exec rm -rf '{}' +

###

FROM python:3.6.5-alpine3.7

ENV PATH=$PATH:/root/.local/bin
ENV FLASK_ENV=production
ENV FLASK_APP=app.py

WORKDIR /usr/src/app/

RUN apk add --no-cache --virtual .run-deps \
    ca-certificates \
    curl \
    openssl \
    zlib

COPY --from=builder /root/.local/ /root/.local/
COPY . .

EXPOSE 8000

CMD ["uwsgi", "--ini", "config/uwsgi.ini", "--single-interpreter", "--enable-threads", "--http", ":8000"]
