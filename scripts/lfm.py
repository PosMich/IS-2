__author__ = "Eschbacher - Poschacher"

import urllib

LFM_API_KEY = "4cb074e4b8ec4ee9ad3eb37d6f7eb240"
LFM_API_URL = "http://ws.audioscrobbler.com/2.0/"

"""
    method = lfm api method
    params = dictionary (where the key is the required param in lfm api)

    example call in code:
        params = {
            "country": "spain"
        }

        content = lfm.call("geo.getTopArtists", params)
"""

def call(method, **kwargs):
    url = LFM_API_URL + "?method=" + method

    for key, value in kwargs.get("params", {}).iteritems():
        param = "&{0}={1}".format(key, urllib.quote(value))
        url += param

    url += "&format=json&api_key={0}".format(LFM_API_KEY)

    print "Calling:\t" + url


    return urllib.urlopen(url).read()

LOCATIONS = [
    "Albania",
    "Andorra",
    "Austria",
    "Belarus",
    "Belgium",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Faroe Islands",
    "Finland",
    "France",
    "Germany",
    "Gibraltar",
    "Greece",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Malta",
    "Moldova",
    "Monaco",
    "Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "San Marino",
    "Serbia",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
    "Ukraine",
    "United Kingdom",
    "Isle of Man",
    "Montenegro"
]
