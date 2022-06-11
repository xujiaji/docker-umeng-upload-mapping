FROM python:3.8-slim-buster
RUN pip3 install requests
COPY . /
CMD python3 upload_mapping.py ${apiKey} ${apiSecurity} ${dataSourceId} ${appVersion} ${mappingFilePath}

