# pull base image
FROM python:3.6

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHON UNBUFFERED 1

# set working directory
WORKDIR /legal_saas_app

# install dependencies
COPY requirements.txt /legal_saas_app/
RUN pip install -r requirements.txt

# Copy project
COPY . /legal_saas_app/