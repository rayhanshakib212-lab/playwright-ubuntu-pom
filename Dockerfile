FROM python:3.14-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir \
    pytest \
    pytest-playwright \
    allure-pytest \
    pytest-rerunfailures \
    pytest-xdist

RUN playwright install --with-deps chromium firefox webkit

CMD ["pytest"]