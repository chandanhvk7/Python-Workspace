import requests
from chanutils import dirr
from pprint import pprint

def main():
    apikey='aa9e49f'
    search_text=input('Enter a movie title to search:')
    url=f'http://omdbapi.com/?s={search_text}&apikey={apikey}'

    resp=requests.get(url)
    if resp.status_code==200:
        resp_json=resp.json()
        print(f'found {resp_json["totalResults"]} movies with "{search_text}" in the title')
        movie =resp_json["Search"]
        for index,each_movie in enumerate(movie):
            print(index+1,each_movie["Title"])

if __name__=="__main__":
    main()