import datetime
import json
import urllib.request

def url_builder(lat, lon):
    api = ""
    unit = "metric"

    return 'https://api.openweathermap.org/data/4.0/onecall/current'\
        + '?units=' + unit +\
        + '&APPID=' + api  +\
        + '&lat=' + str(lat)+\
        + '&lon=' + str(lon) 
    
    

def fetch_data(full_url):
    url = urllib.request.urlopen(full_url)
    output = url.read().decode('utf-8')
    return json.loads(output)


def time_converter(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).\
    strftime('%Y-%m-%d %H:%M:%S')