### I used this example from the book to try and understand what was happening
### Next I will try to follow this example and come up with my own program

import webbrowser
import json
from urllib.request import urlopen

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month and day; like 20150525: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)

response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)

try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("Should appear in your browswer now.")
    webbrowser.open(old_site)
except:
    print("sorry, no luck finding the site.")
