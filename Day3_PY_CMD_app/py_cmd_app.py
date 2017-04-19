"""

Name : Python Command Line application
Author: Benjamin Wacha
Email: bmwachajr
Disc: A python cmd app that taps a dictionry api to get meaning of words.

"""
import requests
import json

def get_data(string):
  #url = 'http://api.wordnik.com:80/v4/word.json/angry/definitions?limit=200&includeRelated=false&sourceDictionaries=webster&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
  url = 'http://api.wordnik.com:80/v4/word.json/'+string+'/definitions?limit=200&includeRelated=true&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'

  resp = requests.get(url)
  if resp.status_code != 200:
      #Something went wrong
      print('GET Failed code: {}'.format(resp.status_code))
  else :
    return resp.text
    
def main:
  print("This is a dictionary app."
  print('####################################################'))
  
  word = input("Enetr a word, to get its definition")
  
  print(get_data(word))

  