import requests 
import os

url = 'https://app.ticketmaster.com/discovery/v2/events'

API_KEY = os.environ['TICKETMASTER_KEY']

payload = API_KEY

res = requests.get(url, params=payload)

# this is our dictionary 
data = res.json()

print("*******")
print(data)
print("*******")
# events = data['_embedded']['events'] # list
# events = []
# check = data.get('_embedded', events)

# how to avoid a KeyError
if '_embedded' in data:
  event = data['_embedded']['genre']
else:
  event = []

# event = events[0] # dictionary
#if event :

# save by keys
keys = event.keys()

# saving events' dates
event_dates = keys['dates']

payload['postalCode'] = '94102'