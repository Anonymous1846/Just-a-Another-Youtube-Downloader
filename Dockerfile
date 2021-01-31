FROM python:3-onbuild

RUN pip install --upgrade pip && \
    pip install pytube && \
    pip install pyfiglet

CMD ["python","./main.py"]
