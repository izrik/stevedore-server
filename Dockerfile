
FROM python:3.8.1-apline3.10



RUN mkdir -p /opt/stevedore
WORKDIR /opt/stevedore

COPY app.py \
     requirements-lock.txt \
     /opt/stevedore

RUN pip install -r requirements.txt

CMD ["flask", "run"]
