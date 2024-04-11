FROM python:3.11-slim

WORKDIR /app

COPY consumer.py .

RUN pip install kafka-python

# Run the Python script when the container starts
CMD ["python", "consumer.py"]