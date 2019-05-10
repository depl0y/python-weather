import os
from classes.daydata import DayData
from influxdb import InfluxDBClient
from classes.tail import Tail
from classes.downloader import Downloader
from classes.progressbar import Progressbar

weather_station = os.getenv('WEATHER_STATION', 278)

host = os.getenv('HOST')
port = os.getenv('PORT', 8086)
database = os.getenv('DATABASE', 'historical')

if not host:
    print("HOST not defined as environment variable")
    exit(2)

print(f"Downloading data for station {weather_station}")
input_file = Downloader.download(weather_station)

if not input_file:
    print("Downloading or unzipping went wrong")
    exit(2)

print(f"Downloaded '{input_file}'.")

lines = Tail.get(input_file, 1460)
print(f"Tailing file, got {len(lines)} items")

client = InfluxDBClient(host, port, ssl=False,
                        verify_ssl=False, database=database)
client.drop_database(database)

print(f"Dropped previous database, resetting")

client.create_database(database)
client.create_retention_policy('two_year', '1460d', 3, default=True)

print(f"Starting import in InfluxDB")

Progressbar.loadingBar(0, len(lines), 60)

index = 0
skipped = 0
imported = 0

for line in lines:
    parts = line.split(',')
    line_prefix = parts[0].strip()
    if line_prefix == str(weather_station):
        data = DayData.from_parts(parts)

        if data:
            json = data.toJson()

            try:
                client.write_points(json, time_precision="s")
                imported += 1
            except:
                skipped += 1

    index += 1
    Progressbar.loadingBar(index, len(lines), 60)

print("")
print(f"Done importing, {imported} imported")
print(f"Skipped {skipped} items")
