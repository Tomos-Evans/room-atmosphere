import requests

import time
#print(requests.post('http://127.0.0.1:5000/alarm/raise'))
time.sleep(4)

print(requests.post('http://pi:5000/alarm/raise'))
time.sleep(20)

#print(requests.post('http://127.0.0.1:5000/alarm/raise'))

print(requests.post('http://pi:5000/alarm/lower'))
