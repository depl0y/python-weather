FROM python:3
ADD weather/ /
RUN pip install influxdb
CMD [ "python", "./parse-weather.py" ]