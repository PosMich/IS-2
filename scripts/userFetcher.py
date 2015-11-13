import csv
import urllib
import json
import os
import pprint

LASTFM_API_KEY = "4cb074e4b8ec4ee9ad3eb37d6f7eb240"
LASTFM_API_URL = "http://ws.audioscrobbler.com/2.0/"

USER_FILE = "./../Part_A/lastfm_users_5.csv"
OUTPUT = "./user/"

def readFile(path):
    users = []
    with open(path, "r") as file:
        userFile = csv.reader(file, delimiter="\t")
        for user in userFile:
            users.append(user[0])
    pprint.pprint(locals())
    return users

def lfm_api_call_getinfo(user):
    url = LASTFM_API_URL + "?method=user.getinfo&user=" + urllib.quote(user) + \
          "&format=json" + "&api_key=" + LASTFM_API_KEY
    content = urllib.urlopen(url).read()
    return content


if __name__ == "__main__":
    if not os.path.exists(OUTPUT):
        os.makedirs(OUTPUT)

    users = readFile(USER_FILE)

    for user in users:
        userInfo = lfm_api_call_getinfo(user)


        currentFile = OUTPUT + user + '.json'
        currentFileOpen = open(currentFile, 'w')
        currentFileOpen.write(userInfo)
        currentFileOpen.close()

        userInfo = json.loads(userInfo)
        print userInfo
        print userInfo["user"]["name"]
        print userInfo["user"]["playcount"]

        # pprint.pprint(locals())
