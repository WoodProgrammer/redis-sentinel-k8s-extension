FROM python:latest
RUN pip3 install redis
RUN pip3 install kubernetes
RUN pip3 install PyYaml
WORKDIR /opt/
COPY update_svc.py .
COPY redis_svc.py .