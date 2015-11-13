import urllib
import pprint
import json

LFM_API_KEY = "4cb074e4b8ec4ee9ad3eb37d6f7eb240"
LFM_API_URL = "http://ws.audioscrobbler.com/2.0/"

"""
    method = lfm api method
    params = dictionary (where the key is the required param in lfm api)
"""
def call(method, params):
    url = LFM_API_URL + "?method=" + method

    for key, value in params.iteritems():
        param = "&{0}={1}".format(key, value)
        url += param

    url += "&api_key={0}".format(LFM_API_KEY)

    return urllib.urlopen(url).read()

if __name__ == "__main__":

    params = {
        "country": "spain"
    }

    content = call("geo.getTopArtists", params)
    pprint.pprint(locals())
