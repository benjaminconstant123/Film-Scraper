import requests
from bs4 import BeautifulSoup

# URL de la page
url = "https://www.themoviedb.org/movie"

# Envoi d'une requete HTTP
reponse = requests.get(url)

if reponse.status_code == 200:
    print('requete good')

    soup = BeautifulSoup(reponse.text, 'html.parser')

    # Trouver les éléments contenant les titres de films et les affiches
    movies = soup.select('.card.style_1 .content')
    posters = soup.select('.card.style_1 .image')
    
    for index, movie in enumerate(movies):
        title = movie.find('h2').text.strip()
        poster_url = posters[index].find('img')['src']
        print(f'Titre: {title}')
        print(f'Affiche: {poster_url}')

else:
    print('requete fail')
    print('Code d\'état HTTP:', reponse.status_code)