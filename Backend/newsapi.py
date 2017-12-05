import requests
import json

def getnews():
    r = requests.get("https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=c7c26ec359ee4b808583307c59852ec6")
    data = json.loads(r.text)
    return(data['articles'][0]['title'])