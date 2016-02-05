####################################
#
#  Dockerfile for Tangela
#  v0.1 - By Moloch
# 
####################################
FROM python:2-onbuild
MAINTAINER moloch

# Make a directory
RUN mkdir -p /opt/tangela

# Copy application into container
ADD . /opt/tangela
WORKDIR /opt/tangela

# Install the dependancies
RUN pip install -r requirements.txt

# Expose Ports
EXPOSE 80
EXPOSE 443
CMD python server.py

