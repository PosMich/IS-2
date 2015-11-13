import urllib

LFM_API_KEY = "4cb074e4b8ec4ee9ad3eb37d6f7eb240"
LFM_API_URL = "http://ws.audioscrobbler.com/2.0/"

def call(method):
    LFM_API_URL + "?method=" + method
