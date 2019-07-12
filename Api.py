import requests
import logging
import json

url = 'https://api.tradegecko.com/'
#payload = open("request.json")
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8','Authorization': 'Bearer TOKEN HERE'}
r = requests.get(url, headers=headers,verify=False)
#print(r.content)

base_uri = 'https://api.tradegecko.com/'
access_token = "TOKEN HERE"
header = {
    'Authorization': 'Bearer ' + access_token,
    'content-type': 'application/json'
}
rsp = None
json = None
base_uri = base_uri
uri = ''
required_fields = []
data = {}
method="GET"
rsp = requests.request(method, base_uri, data={}, headers=header, params=None,verify=False)

#products
base_uri = 'https://api.tradegecko.com/'
print(rsp.status_code)
#logger.info('TRADEGECKO API REQUEST: %s %s \nDATA="%s" \nPARAMS="%s" \nRESPONSE="%s" \nSTATUS_CODE: %s' % (method, uri, data, params, rsp.content, rsp.status_code))
base_uri = base_uri+"products/"
rsp = requests.request(method, base_uri, data={}, headers=header, params=None,verify=False)
print(rsp.json())
