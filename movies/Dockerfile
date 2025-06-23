FROM python:3.12-alpine

WORKDIR /app

COPY ../movies-api /app

RUN pip install -r requirments.txt

EXPOSE 80

CMD ["python", "movies.py"]