FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./migsbyu /app/migsbyu

CMD ["uvicorn", "migsbyu.main:app", "--host", "0.0.0.0", "--port", "8000", "--root-path", "/"]
