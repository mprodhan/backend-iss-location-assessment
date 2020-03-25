#!/usr/bin/env python
import requests
import time
import turtle

__author__ = 'mprodhan/yabamov/denas/madarp'

base_url = "http://api.open-notify.org"

def astro_name():
    r = requests.get(base_url + "/astros.json")
    r.raise_for_status()
    return r.json()['people']


def iss_location():
    req = requests.get(base_url + "/iss-now.json")
    req.raise_for_status()
    req_coord = req.json()['iss_position']
    req_lon = float(req_coord['longitude'])
    req_lat = float(req_coord['latitude'])
    return (req_lat, req_lon)

def compute_risetime(lat, lon):
    coord = {'lat': lat, 'lon': lon}
    r = requests.get(base_url + '/iss-pass.json', params=coord)
    risetime = r.json()['response'][0]['risetime']
    time_stamp = time.ctime(risetime)
    # print(req_obj)
    return risetime
    # unable to get time_stamp; ran it on python interpreter and it prints

def world_map(lat, lon):
    # iss_location()
    # lon = req_json['iss_position']['longitude']
    # window Setup
    iss = turtle.Turtle()
    screen = turtle.Screen()
    screen.register_shape("iss.gif")
    screen.setup(720, 360)
    screen.bgpic("map.gif")
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss.penup()
    iss.shape("iss.gif")
    iss.goto(lon, lat)
    turtle.done()

def main():
    astro_dict = astro_name()
    for a in astro_dict:
        print(a)
    print('Total number of faculty in ISS: ' + str(len(astro_dict)))
    lat, lon = iss_location()
    print(f"The coordinates of the ISS: lat = {lat}, lon = {lon}")
    indy_lat = 39.79100
    indy_lon = -86.148003
    compute_risetime(indy_lat, indy_lon)
    world_map(lat, lon)


if __name__ == '__main__':
    main()

