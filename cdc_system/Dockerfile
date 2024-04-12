FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

RUN pip install spark kafka-python pyspark

WORKDIR /app

COPY . .

# Run the Python script when the container starts
# CMD ["python", "main.py"]
CMD ["tail", "-f", "/dev/null"]