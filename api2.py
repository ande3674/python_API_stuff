import webbrowser
import json
from urllib.request import urlopen
import requests

r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
r.text

# Convert to a python dictionary
data = json.loads(r.text)

# Loop thru the result
for item in data['data']['items']:
    print("Video Title: %s" % (item['title']))
    print("Video Category: %s" % (item['category']))

    print("Video ID: %s" % (item['id']))

    print("Video Rating: %f" % (item['rating']))

    print("Embed URL: %s" % (item['player']['default']))

    print(" ")