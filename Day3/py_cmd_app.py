"""

Name : Python Command Line application
Author: Benjamin Wacha
Email: bmwachajr
Disc: A python cmd app that taps a dictionry api to get meaning of words.

"""
import requests


def get_data(string):
  url = 'https://services.aonaware.com/DictService/DictService.asmx/Define?word=' + string +' HTTP/1.1'
  resp = requests.get(url)
  if resp.status_code != 200:
      #Something went wrong
      raise ApiError('GET Failed code: {}'.format(resp.status_code))
  for Item in resp.json():
      #print('{} {}'.format(todo_item['id'], todo_item['summary']))
      print "yolo"

print (get_data('angry'))