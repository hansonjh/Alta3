#!/usr/bin/python3

import requests

URL= "http://api.open-notify.org/astros.json"
URL2= 'http://api.open-notify.org/iss-now.json'

def main():
    # requests.get() requests info from the URL
    # .json() method transforms that data into a Pythonic dictionary!
    sliceme= requests.get(URL).json()
    sliceme2= requests.get(URL2).json()
                      
    print('People in space:', sliceme['number'])
    for y in sliceme['people']:
        print(y['name'], 'is on the', y['craft'])
    
    print('CURRENT LOCATION OF THE ISS:')
    print('Lon:', sliceme2['iss_position']['longitude'])
    print('Lat', sliceme2['iss_position']['latitude'])

main()
