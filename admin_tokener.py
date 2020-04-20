import http.client
import json
import os

conn = http.client.HTTPSConnection("dev-55ehn3as.eu.auth0.com")
payload = "{\"client_id\":\"ah64JSWyH2nZtFiBPPcFp06zEI8TIJDR\",\"client_secret\":\"yx9aEfq6LoiMp5zZ83LF6X8e6ZG-1tYHZLbHRW-TFErpBhaX8APi8ROHhO7vFKq4\",\"audience\":\"casting_agency\",\"grant_type\":\"client_credentials\"}"
headers = {'content-type': "application/json"}
conn.request("POST", "/oauth/token", payload, headers)
res = conn.getresponse()
data = res.read()
token = json.loads(data)['access_token']
