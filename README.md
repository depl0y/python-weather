# python-weather
A tiny Docker, that pulls historical weather data from the KNMI and pushes that data in InfluxDB.

## Options
| Name | Description | Optional? | Default value |
|---|---|---|---|
|HOST|The hostname of the Influx DB|Required|-|
|PORT|The port of InfluxDB|Yes|8086|
|DATABASE|The database name|Yes|historical|
|WEATHER_STATION|The weather station ID|Yes|278|

## Important
- Every time it runs, it drops the old database and creates a new one. 
- There is only 1 retention policy in the database, which stores the data for 2 years.