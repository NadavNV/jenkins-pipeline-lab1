FROM python:3.12-alpine

WORKDIR /app_test

COPY . /app_test

RUN pip install -r requirments.txt

CMD ["python", "test.py"]