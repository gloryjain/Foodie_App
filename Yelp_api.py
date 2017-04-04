#!/usr/bin/python
#Author  : Glory Jain

import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

location=raw_input("What's your location? Ex. zip code, city: ")
term=raw_input("What type of restaurant are you trying to go to? Ex. ethiopian: " )
pricing_filters=raw_input("Enter how much money you're willing to spend! 1 for fast food, 4 for very pricey $$$")
sort_by=raw_input("Sort by? ex. rating : ")

params = {'location': location,
          'term': term,
          'pricing_filter': pricing_filters,
          'sort_by': sort_by 
         }


app_id = 'FZATfc4ra4iT70SRsPW44g'
app_secret = 'irZsZ5NChA85wb1TDJFxs2ukuwwWRcH6WGVpJglg828cQDjSp9IHW9ZvGSbPKtWW'
data = {'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret}

token = requests.post('https://api.yelp.com/oauth2/token', data=data)
access_token = token.json()['access_token']
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'bearer %s' % access_token}

resp = requests.get(url=url, params=params, headers=headers)

#import pprint
x=resp.json()['businesses']
print('~~~~~~~~~~~~~Finding Recommended Restaurants (*^◇^)_旦~~~~~~~~~~')
for e in x:
   if isinstance(e, dict):
      print("Name : "+e[u'name'])
      print("Address :")
      for i in e[u'location'][u'display_address']:
          print(i)
      print("\n")
