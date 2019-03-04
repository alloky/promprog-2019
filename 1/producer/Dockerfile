FROM python:3.4-alpine
COPY . /producer
RUN pip install -r /producer/requirements.txt
ENV PYTHONUNBUFFERED=1
CMD ["python", "/producer/producer.py"]