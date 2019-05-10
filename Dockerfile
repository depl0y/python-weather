FROM python:3
MAINTAINER Wim Haanstra <wim@wim.me>

ADD weather/ /
RUN pip install influxdb
CMD [ "python", "./parse-weather.py" ]
