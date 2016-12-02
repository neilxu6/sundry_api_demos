# -*- coding: utf-8 -*-

# api主页：http://freegeoip.net/
# api格式：freegeoip.net/{format}/{IP_or_hostname}
# format类型：
# （1）csv：freegeoip.net/csv/{IP_or_hostname}
# （2）xml：freegeoip.net/xml/{IP_or_hostname}
# （3）json:freegeoip.net/json/{IP_or_hostname}

import requests
import csv

ip_or_host = '183.192.90.57'

def get_ip_info_from_json(ip_or_host):
    api='http://freegeoip.net/json/' + ip_or_host
    r = requests.get(api)
    data = r.json()
    # print data
    print (ip_or_host + '位于' + str(data['time_zone']))

def get_ip_info_from_xml(ip_or_host):
    api = 'http://freegeoip.net/xml/' + ip_or_host
    r=requests.get(api)
    data=r.text
    print data


# 有错误，待修改
def get_ip_info_from_csv(ip_or_host):
    api = 'http://freegeoip.net/xml/' + ip_or_host
    r=requests.get(api)
    data=csv.reader(r)
    for line in data:
        print line

get_ip_info_from_csv(ip_or_host)
