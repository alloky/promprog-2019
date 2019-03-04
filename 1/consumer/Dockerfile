FROM python:3.4-alpine
COPY . /consumer
RUN pip install -r /consumer/requirements.txt
ENV PYTHONUNBUFFERED=1
CMD ["python", "/consumer/consumer.py"]