FROM python:3.8-slim-buster

RUN mkdir /server1
COPY . /server1
WORKDIR /server1

RUN pip install -r requirement.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "Server3.py" ]