from enum import Enum
import time
import math
import requests
import os

#import requests



#import numpy as np

class Curve(Enum):
    SIN = 1

start = 0
hint = "There are environment variables missing. Run the container with the splunk-hec-url and the splunk-token variables. Example: docker run --name testi --network host -e URL='https://127.0.0.1:8088/services/collector' -e TOKEN='9f830b6f-94cd-4b5a-8d60-d69c9f953605' testi\r\nExiting!"
debug = False
if debug != True:
    if os.environ.get('URL') is not None:
        url = os.environ.get('URL')
        url = url.replace("'","")
    else:
        print (hint)
        exit()
    if os.environ.get('TOKEN') is not None:
        token = os.environ.get('TOKEN')
        token = token.replace("'","")
    else:
        print (hint)
        exit()
    if os.environ.get('KEY') is not None:
        key = os.environ.get('KEY')
    else:
        key="Value"
else:
    url ="https://127.0.0.1:8088/services/collector"
    token = "9f830b6f-94cd-4b5a-8d60-d69c9f953605"
    key="Value"
headers = {
    'Authorization': 'Splunk ' + token,
}
print("Url: " + url)
print("Token: " + str(token))
print("Key: " + str(key))
while True:
    #x = np.arange(sample)
    #y = np.sin(2 * np.pi * f * x / Fs)
    value = math.sin(start) 
    
    data = '{"event": "{\\"'+key+'\\":' + str(value) + '}", "sourcetype": "_json"}'
    print (data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    start += 0.1
    time.sleep(1)