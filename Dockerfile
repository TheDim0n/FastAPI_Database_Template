FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt && \
    find / -xdev -name *.pyc -delete

COPY . .

EXPOSE 8000

CMD ["python", "run.py"]