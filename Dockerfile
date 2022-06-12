FROM python:3.8-slim-buster
RUN pip3 install requests
COPY . /
COPY upload_mapping.sh /bin/upload_mapping
RUN chmod +x /bin/upload_mapping