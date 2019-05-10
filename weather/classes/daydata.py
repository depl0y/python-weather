import constants

class DayData:
    def __init__(self, parts):
        from datetime import datetime        

        self.station_id = int(parts[constants.STATION_ID])
        self.date = datetime.strptime(parts[constants.DATE_COLUMN], '%Y%m%d')

        self.average_windspeed = float(parts[constants.AVERAGE_WINDSPEED].strip()) / 10
        self.highest_windspeed = parts[constants.HIGHEST_WINDSPEED].strip()
        self.highest_windspeed_hour = parts[constants.HIGHEST_WINDSPEED_HOUR].strip()
        self.lowest_windspeed = parts[constants.LOWEST_WINDSPEED].strip()
        self.lowest_windspeed_hour = parts[constants.LOWEST_WINDSPEED_HOUR].strip()

        self.average_temperature = float(parts[constants.AVERAGE_TEMPERATURE].strip()) / 10
        self.minimum_temperature = parts[constants.MINIMUM_TEMPERATURE].strip()
        self.minimum_temperature_hour = parts[constants.MINIMUM_TEMPERATURE_HOUR].strip()
        self.maximum_temperature = parts[constants.MAXIMUM_TEMPERATURE].strip()
        self.maximum_temperature_hour = parts[constants.MAXIMUM_TEMPERATURE_HOUR].strip()

    def timestamp(self):
        return self.date.timestamp()

    def toJson(self):
        json = [
            {
                "measurement": "temperature",
                "tags": {
                    "station": self.station_id
                },
                "time": self.date.strftime("%Y%m%dT%H%M%SZ"),
                "fields": {
                    "value": self.average_temperature
                }
            },
            {
                "measurement": "windspeed",
                "tags": {
                    "station": self.station_id
                },
                "time": self.date.strftime("%Y%m%dT%H%M%SZ"),
                "fields": {
                    "value": self.average_windspeed
                }
            }
        ]
        return json
                    

    @staticmethod
    def from_parts(parts):
        if not DayData.valid_data(parts):
            return None
        else:
            d = DayData(parts)
            return d

    @staticmethod
    def valid_data(parts):
        import constants
        from datetime import datetime        

        for column in constants.COLUMNS:
            if not parts[column] or parts[column].strip() == '':
                return False

        date = datetime.strptime(parts[constants.DATE_COLUMN], '%Y%m%d') 
        if not date or date == '':
            return False           

        return True
        