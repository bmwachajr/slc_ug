"""

Name : Python Command Line application
Author: Benjamin Wacha
Email: bmwachajr
Disc: A python cmd app that taps a dictionry api to get meaning of words.

"""
import requests
import json

def get_data(string):
  url = 'https://glosbe.com/gapi/translate?from=eng&dest=swh&format=json&phrase='+string+'&pretty=true'
  resp = requests.get(url)
  if resp.status_code != 200:
      #Something went wrong
      print('GET Failed code: {}'.format(resp.status_code))
  else :
    for item in resp.json():
      print('{}'.format(item))
  return resp.headers
print (get_data('Hello'))