# -*- coding: utf-8 -*-

import requests

key='AIzaSyDI7tpT0MJlJVrSSp3L_B_yTh4BXZNjv9s'
api='https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJN1t_tDeuEmsRUsoyG83frY4&key='+key
proxies='http://178.34.176.86:8080'
r=requests.get(api,proxies=proxies)

data=r.json()
print data