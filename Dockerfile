# Use the official image as a parent image.
FROM geerlingguy/docker-ubuntu1804-ansible

USER root

# Set the working directory.
WORKDIR /home

# Copy the file from your host to your current location.
COPY requirements.txt requirements.txt

# Run the command inside your image filesystem.
RUN pip3 install wheel
RUN pip3 install -r requirements.txt