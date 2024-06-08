import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = "https://www.tameteo.com/meteo_Toulouse-Europe-France-Haute+Garonne-LFBO-1-26128.html"

# Envoyer une requête GET à l'URL
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Utiliser BeautifulSoup pour analyser le contenu HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trouver l'élément strong avec la classe temp
    temp_element = soup.find('span', class_='dato-temperatura changeUnitT')

    # Vérifier si l'élément a été trouvé
    if temp_element:
        # Extraire le contenu textuel et le nettoyer
        temperature = temp_element.text.strip()

        # Afficher la température
        print("Température:", temperature)
    else:
        print("Aucune température trouvée.")
else:
    print("Échec de la requête.")
