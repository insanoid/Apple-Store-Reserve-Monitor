FROM python:3.11

COPY ./* /app/

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD ["python", "monitor.py"]


