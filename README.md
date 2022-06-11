Requirements
------------
python(>=2.7)
requests


Examples
--------
test.py


Docker
--------
https://hub.docker.com/repository/docker/xujiaji/umeng-upload-mapping

docker run \
-e apiKey=7134455 \
-e apiSecurity=k3fgz9r5Pd \
-e dataSourceId=4bbf2736f1f55691100011e3 \
-e appVersion=10.10.10 \
-e mappingFilePath=proguardMapping.txt \
umeng-upload-mapping:v1.0