import requests
import json

def osm_requests(city):
    pyload_osm = {
    'q': city,
    'format':'json',
    'addressdetails':1,
    'limit':1,
    'polygon_svg':1
    }
    response_osm = requests.get('https://nominatim.openstreetmap.org/search/?', params=pyload_osm)

    if response_osm.ok:
        data = (response_osm.json())[0]
        return data
    else:
        return None


def osm_data(city):
    data = osm_requests(city)
    try:
        geolocation = [data['lat'], data['lon']]
        return geolocation
    except Exception as e:
        return e


def airly_data(city):
    coords = osm_data(city)
    lat = coords[0]
    lon = coords[1]

    headers = {
    'Accept':'application/json',
    'apikey':'tlh6YpcTCMSYIKoUJvJqK7yfVBy2QbbC'
    }

    pyload_airly ={
    'indexType':'AIRLY_CAQI',
    'lat':lat,
    'lng':lon,
    'maxDistanceKM': 6,

    }

    response_airly = requests.get('https://airapi.airly.eu/v2/measurements/nearest?', headers=headers, params=pyload_airly)
    print(json.loads(response_airly.text))
    json_r = json.loads(response_airly.text)['current']
    return json_r
