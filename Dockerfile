# Use the official image as a parent image.
FROM python:3.7-alpine3.9

# Set the working directory.
WORKDIR /home

# Copy the file from your host to your current location.
COPY requirements.txt requirements.txt
COPY . .

# Run the command inside your image filesystem.
RUN pip install --upgrade pip
RUN pip install wheel

RUN apk update 
RUN apk add gcc musl-dev libffi-dev openssl-dev
# RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
#     && pip install cython \
#     && apk del .build-deps gcc musl-dev

RUN pip install -r requirements.txt