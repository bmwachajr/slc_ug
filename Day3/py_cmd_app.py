"""

Name : Python Command Line application
Author: Benjamin Wacha
Email: bmwachajr
Disc: A python cmd app that taps a dictionry api to get meaning of words.

"""
import requests


def get_data(string):
  url = 'https://wordsapiv1.p.mashape.com/words/'+string+'/definitions'
  resp = requests.get(url)
  if resp.status_code != 200:
      #Something went wrong
      print('GET Failed code: {}'.format(resp.status_code))
  for Item in resp.json():
      #print('{} {}'.format(todo_item['id'], todo_item['summary']))

print (get_data('angry'))