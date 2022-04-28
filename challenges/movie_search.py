#!/usr/bin/env python3
import requests
import wget

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

def main():
    choice= input("Enter a movie title:\n>")
    
    full_url= URL + choice
    
    movies= requests.get(full_url).json()

    #print(movies)
    print(full_url)

    count = 0
    # the dictionary is "movies"
    for x in movies['Search']:
        if x['Type'] == 'movie':
            print(x['Title'], 'was released in', x['Year'])
            
            if count == 0:
                poster_url = x['Poster']
                wget.download(poster_url, '/home/student/static/')
                print('\nDownloaded a poster for', x['Title'])
                count += 1

if __name__ == "__main__":
    main()
