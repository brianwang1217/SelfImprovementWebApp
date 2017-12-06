import requests
from newsapi import send_mail

r = requests.post("http://api.forismatic.com/api/1.0/", data={"method": "getQuote", "format" : "text", 'key': 111, "lang": 'en'})

send_mail(r.text, "Quote of the Day")

