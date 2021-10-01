# syntax=docker/dockerfile:1
FROM python:3.7
COPY egen-project-1-327215-261475be0596.json egen-project-1-327215-261475be0596.json
COPY pub_docker.py pub_docker.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD [ "python3", "pub_docker.py"]