__author__ = "Eschbacher - Poschacher"

import lfm
import os
import json
import pprint

OUTPUT_DIR = "../data/users"
OUTPUT_FILE_NAME = "users"
if __name__ == "__main__":

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    uniqueArtists = {}
    uniqueUsers = []

    """
        The following code is not working because last.fm api call artist.gettopfans returns an error with invalid method.
    """
    # for i, value in enumerate(lfm.LOCATIONS):
    #     print "current country processed is: {0}".format(value)
    #     params = {
    #         "country": value
    #     }

    #     artists = lfm.call("geo.gettopartists", params = params)
    #     artistsTree = json.loads(artists)
    #     artists = artistsTree["topartists"]["artist"]

    #     print "number of available top artists: {0}".format(len(artists))

    #     for artist in artists:
    #         mbid = artist["mbid"]

    #         if(not mbid in uniqueArtists):
    #             uniqueArtists[mbid] = mbid

    #             params = {
    #                 "mbid": mbid
    #             }
    #             fans = lfm.call("artist.gettopfans", params = params)
    #             fansTree = json.loads(fans)

    #             if "topfans" in fansTree:
    #                 if "user" in fansTree["topfans"]:

    #                     firstTopFan = fansTree["topfans"]["user"][0]["name"]
    #                     if(not (firstTopFan in uniqueUsers)):
    #                         uniqueUsers.append(firstTopFan)
    #                         print "first top fan: {0}".format(firstTopFan)


    print "numbers of users: {0}".format(len(uniqueUsers))
