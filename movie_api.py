import urllib.request as request
from urllib.parse import quote
import json

def main():

    key = '14b534c6'
    movie = input("Enter a movie to search for: ")

    url = 'http://www.omdbapi.com/?apikey=%s&t=%s' % (key, movie)

    response = request.urlopen(url)

    responseJson = response.read().decode('utf-8')

    print(responseJson)

    parsedJson = json.loads(responseJson)

    print(parsedJson["Title"], "movie plot: ")
    plot = parsedJson["Plot"]
    print(plot)

main()