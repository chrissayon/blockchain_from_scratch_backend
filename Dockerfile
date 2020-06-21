# Use the official image as a parent image.
FROM ubuntu:bionic

# Install python
RUN apt-get update
RUN apt-get -y install python3.7 python3-pip
# Next version do: apt-get -y install python3-pip  python3.7-dev

# Set the working directory.
WORKDIR /home

# Copy the file from your host to your current location.
COPY requirements.txt requirements.txt

# Run the command inside your image filesystem.
RUN pip3 install wheel
RUN pip3 install -r requirements.txt