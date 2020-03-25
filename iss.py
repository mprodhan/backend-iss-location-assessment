#!/usr/bin/env python
import requests
import json
import time
import turtle

__author__ = 'mprodhan/yabamov'

def astro_name():
    get_a = "http://api.open-notify.org/astros.json"
    r = requests.get(get_a)
    json_r = json.loads(r.text)
    for info in json_r['people']:
        print(info)
    print('Total number of faculty in ISS: ' + str(json_r['number']))

def iss_location():
    get_loc = "http://api.open-notify.org/iss-now.json"
    url = 'http://maps.googleapis.com/maps/api/geocode/json'
    api_key = "AIzaSyC_6q5u5NeyvzFTHIZzPleWL5n-cUulVU0key"
    
    req = requests.get(get_loc)
    req_json = json.loads(req.text)
    req_coord = req_json['iss_position']
    req_lon = req_json['iss_position']['longitude']
    req_lat = req_json['iss_position']['latitude']
    print("The coordinates of the ISS: " + req_lon, req_lat)
    
    place =input(req_coord)
    req_obj = requests.get(url + 'coordinates =' +
                place + '&key =' + api_key)
    python_obj = req_obj.json()
    t = req_json['timestamp']
    time_stamp = time.ctime(t)
    print(req_obj, "at", time_stamp)
    # unable to get time_stamp; ran it on python interpreter and it prints

def world_map():
    pass

def main():
    astro_name()
    iss_location()
    world_map()


if __name__ == '__main__':
    main()

