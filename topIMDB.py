import requests 
from bs4 import BeautifulSoup

"""
This program pulls the all-time top 100 imdb movies and prints them to the console.

Author: Aidan Hackett
"""
print("Hello!")

# decision = input("Would you like a movie suggestion? (yes/no): ")

# # Validate input
# while decision != "yes" and decision != "no":
#     decision = input("yes or no?")

# if decision == "no":
#     print("bye!")
#     quit

# if decision == "yes":
#     print("fuck yeah")

# Select IMDB all-time top 100 & create beautifulsoup
page = requests.get('https://www.imdb.com/list/ls055592025/')
soup = BeautifulSoup(page.text, 'html.parser')

# Extract h3 tag with titles
film_list = soup.find_all(class_='lister-item-header') 

for film in film_list:
    
    film.span.decompose() # Remove index num
    film.a.unwrap() # Remove a tags 
    film.span.decompose() # Remove year 

    filmName = film.prettify() # Format properly 
    print (filmName.splitlines()[1]) # Print title of film




