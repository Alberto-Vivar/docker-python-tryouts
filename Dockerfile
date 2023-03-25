FROM python:3

WORKDIR /usr/src/app

RUN pip3 install --upgrade pip
COPY requirements.txt ./
COPY run.py ./
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "run.py"]
