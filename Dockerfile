FROM python:2.7

ARG TINI_VERSION=v0.16.1
ARG TINI_SHA=d1cb5d71adc01d47e302ea439d70c79bd0864288

# Install Tini
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc /tini.asc
RUN gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \
    && gpg --verify /tini.asc \
    && chmod +x /tini

RUN pip install gunicorn gevent
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY app /src
WORKDIR /src
EXPOSE 8000

ENTRYPOINT ["/tini","--", "gunicorn", "-k", "gevent", "--bind", "0.0.0.0", "b3censortest:app"]
