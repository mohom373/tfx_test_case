FROM mcr.microsoft.com/devcontainers/python:0-3.7


RUN apt-get update && \
     apt-get install -y neofetch 

RUN --mount=type=cache,target=/root/.cache \
    pip install tensorflow tfx ipykernel


#COPY requirements.txt test_requirements.txt /tmp/pip-tmp/
#RUN --mount=type=cache,target=/root/.cache \
    #pip install -r /tmp/pip-tmp/test_requirements.txt -r /tmp/pip-tmp/requirements.txt
