FROM python:3.8.8-buster

RUN pip install -r requirements.txt

CMD ["python","./main.py"]
