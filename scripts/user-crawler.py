__author__ = "Eschbacher - Poschacher"

import lfm
import os
import pprint

OUTPUT_DIR = "../data/users"
OUTPUT_FILE_NAME = "users"

if __name__ == "__main__":

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    locations = lfm.call("geo.getmetros")

    # params = {
    #     "country": "spain"
    # }

    # content = lfm.call("geo.getTopArtists", params = params)
