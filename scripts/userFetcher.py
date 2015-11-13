import lfm
import pprint

if __name__ == "__main__":

    params = {
        "country": "spain"
    }

    content = lfm.call("geo.getTopArtists", params)
    pprint.pprint(locals())
