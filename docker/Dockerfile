FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY hello.py .

EXPOSE 80

CMD [ "python", "hello.py" ]



