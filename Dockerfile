# Pull base image
FROM python:3.6

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
WORKDIR /code

# Install dependencies
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt

# Copy project
ADD . /code/
