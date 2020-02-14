FROM python:3.7

RUN mkdir /server1
COPY . /server1
WORKDIR /server1

RUN pip install -r requirement.txt

EXPOSE 5372

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]