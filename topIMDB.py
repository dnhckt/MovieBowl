import requests 
from random import randrange
from bs4 import BeautifulSoup

"""
This program pulls the all-time top 100 imdb movies and prints them to the console.

Author: Aidan Hackett
"""
print("Hello!")

decision = input("Would you like a movie suggestion? (y/n): ")

# Validate input
while decision != "y" and decision != "n":
    decision = input("y or n?")

if decision == "n":
    print("bye!")
    quit

if decision == "y":
    print("Let's see...")


"""     SELECT IMDB MOVIES    """

    # Select IMDB all-time top 100 & create beautifulsoup
    page = requests.get('https://www.imdb.com/list/ls055592025/')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extract h3 tag with titles
    film_list = soup.find_all(class_='lister-item-header') 

    i = 0
    IMDBlist = [] 
    
    # Add films to IMDBlist
    for film in film_list:
        
        film.span.decompose() # Remove index num
        film.a.unwrap() # Remove a tags 
        film.span.decompose() # Remove year 

        filmName = film.prettify() # Format properly 
        IMDBlist.append(filmName.splitlines()[1]) 
        i = i + 1

""" MOVIES FROM MY MOVIE BOWL 

    Rain Man
    The fountain 
    old boy 
    kuso 
    the village 
    airplane
    crank 
    weekend at bernies
    good time 
    django unchained 
    hot tub time machine 
    sixth sense
    unbreakable
    glass
    big fish 
    2001: 
    a space odyssey
    the godfather 
"""

    aidanList = ["", ""]

    randNum = randrange(0, 100, 2)
    print("You should watch" + IMDBlist[randNum] + "!")
