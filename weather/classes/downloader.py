class Downloader:

    @staticmethod
    def download(station_id):
        import os

        zipfile = Downloader.download_zip(station_id)

        if not zipfile:
            print("ZIP file not downloaded")
            return None
        
        if not os.path.exists(zipfile):
            print("ZIP file does not exist")
            return None

        Downloader.extract_zip(zipfile, station_id)
        filename = f"import/{station_id}/etmgeg_{station_id}.txt"

        if not filename:
            print("Extraction failed? File not here")
            return None

        if not os.path.exists(filename):
            print("File not in the expected location.")
            return None

        return filename

    @staticmethod
    def download_zip(station_id):
        import urllib.request

        url = f"https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/daggegevens/etmgeg_{station_id}.zip"

        filename = f"import/{station_id}.zip"
        response = urllib.request.urlretrieve(url, filename)
        return filename

    @staticmethod
    def extract_zip(filename, station_id):
        import zipfile
        extract_directory = f"import/{station_id}/"
        zip_ref = zipfile.ZipFile(filename, 'r')
        zip_ref.extractall(extract_directory)
        zip_ref.close()
