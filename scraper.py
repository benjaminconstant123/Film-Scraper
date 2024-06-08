import requests
from bs4 import BeautifulSoup

# URL de la page à scraper sur TMDb
url = 'https://www.themoviedb.org/movie'

# Envoyer une requête HTTP à l'URL
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver les éléments contenant les titres de films et les affiches
    movies = soup.select('.card.style_1 .content')
    posters = soup.select('.card.style_1 .image img')
    
    for index, movie in enumerate(movies):
        title = movie.find('h2').text.strip()
        poster_url = posters[index]['src']
        print(f'Titre: {title}')
        print(f'Affiche: {poster_url}')
else:
    print('La requête a échoué')
