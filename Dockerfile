# Choose a parent image
FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7

# Set the working directory
WORKDIR /usr/Documents/TestDocker

#Copy requirement.txt
COPY requirements.txt .

#Install packages
RUN pip3 install -r requirements.txt