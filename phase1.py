"""""
import requests
import json
import time

# Liste des villes du Maroc concaténées avec "banque"
villes_maroc = [
    "Casablanca", "Rabat", "Marrakech", "Fès", "Tanger", "Meknès", "Agadir", 
    "Oujda", "Kenitra", "Tetouan", "Safi", "El Jadida", "Beni Mellal", 
    "Nador", "Taza", "Khouribga", "Settat", "Larache", "Ksar El Kebir", 
    "Guelmim", "Berrechid", "Errachidia", "Taroudant", "Ouarzazate", 
    "Sidi Kacem", "Tiflet", "Sidi Slimane", "Youssoufia", "Tan-Tan", 
    "Souk El Arbaa", "Taourirt", "Ouazzane", "Berkane", "Sefrou", 
    "Tiznit", "Azrou", "Midelt", "Skhirat", "Témara", "El Hajeb", 
    "Moulay Abdallah", "Chefchaouen", "Dakhla", "Laayoune", "Smara", 
    "Asilah", "Fnideq", "Martil", "Bouznika", "Sidi Bennour", "Zagora"
]

villes_avec_bank = ["banque" + ville   for ville in villes_maroc]

# Configuration de l'API
url = "https://places.googleapis.com/v1/places:searchText"
headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": "AIzaSyDUTyVkdL9hpCbM5w4KHQDjryeOLoj0d5k",  # Remplacez par votre clé API
    "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.reviews,places.shortFormattedAddress,nextPageToken"
}

# Itérer sur chaque ville dans la liste
for ville_bank in villes_avec_bank:
    print(f"Traitement de la ville : {ville_bank}")
    
    # Initialisation du nextPageToken
    next_page_token = None
    page_number = 1

    while True:
        # Payload de la requête
        data = {
            "textQuery": ville_bank
             
        }

        # Ajouter le nextPageToken s'il existe
        if next_page_token:
            data["pageToken"] = next_page_token

        # Faire la requête API
        response = requests.post(url, json=data, headers=headers)

        # Traiter la réponse
        if response.status_code == 200:
            results = response.json()
            print(f"Page {page_number} pour '{ville_bank}':")
            
            # Sauvegarder les résultats dans un fichier JSON
            with open(f"results_{ville_bank}_page_{page_number}.json", "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=4)

            # Afficher les résultats
            for place in results.get("places", []):
                print(f"Nom: {place.get('displayName', {}).get('text')}")
                print(f"Adresse: {place.get('formattedAddress')}")
                print(f"Note: {place.get('rating')}")
                print(f"Nombre d'avis: {place.get('userRatingCount')}")
                print(f"Nombre d'avis: {place.get('reviews')}")
                print(f"Nombre d'avis: {place.get('shortFormattedAddress')}")
                print("------")

            # Vérifier s'il y a une page suivante
            next_page_token = results.get("nextPageToken")
            if not next_page_token:
                break  # Sortir de la boucle si aucune page suivante

            page_number += 1
            time.sleep(2)  # Attendre 2 secondes entre les requêtes pour respecter les limites de taux
        else:
            print(f"Erreur pour '{ville_bank}': {response.status_code}")
            print(response.text)  # Afficher les détails de l'erreur
            break
"""""

import requests
import json
import time

# Liste des banques
banques = [
    # Banques commerciales
    "Attijariwafa Bank", "Banque Populaire du Maroc (BCP)", "BMCE Bank of Africa",
    "Banque Marocaine pour le Commerce et l'Industrie (BMCI)", "Société Générale Maroc",
    "Crédit du Maroc", "CIH Bank", "Crédit Agricole du Maroc", "Arab Bank Maroc", "CFG Bank",
    # Banques participatives
    "Al Akhdar Bank", "Umnia Bank", "Bank Assafa", "BTI Bank", "Bank Al Tamwil Wa Al Inmaa",

    
     
]

# Liste des villes du Maroc
villes_maroc = [
    "Casablanca", "Rabat", "Marrakech", "Fès", "Tanger", "Meknès", "Agadir", 
    "Oujda", "Kenitra", "Tetouan", "Safi", "El Jadida", "Beni Mellal", 
    "Nador", "Taza", "Khouribga", "Settat", "Larache", "Ksar El Kebir", 
    "Guelmim", "Berrechid", "Errachidia", "Taroudant", "Ouarzazate", 
    "Sidi Kacem", "Tiflet", "Sidi Slimane", "Youssoufia", "Tan-Tan", 
    "Souk El Arbaa", "Taourirt", "Ouazzane", "Berkane", "Sefrou", 
    "Tiznit", "Azrou", "Midelt", "Skhirat", "Témara", "El Hajeb", 
    "Moulay Abdallah", "Chefchaouen", "Dakhla", "Laayoune", "Smara", 
    "Asilah", "Fnideq", "Martil", "Bouznika", "Sidi Bennour", "Zagora"
]

# Configuration de l'API
url = "https://places.googleapis.com/v1/places:searchText"
headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": "AIzaSyDUTyVkdL9hpCbM5w4KHQDjryeOLoj0d5k",  # Remplacez par votre clé API
    "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.reviews,places.shortFormattedAddress,nextPageToken"
}

# Boucle sur chaque ville
for ville in villes_maroc:
    # Boucle sur chaque banque
    for banque in banques:
        query = f"{banque} {ville}"
        print(f"Traitement de : {query}")
         # Initialisation du nextPageToken
        next_page_token = None
        page_number = 1

        while True:
            # Payload de la requête
            data = {
                "textQuery": query
            }
            # Ajouter le nextPageToken s'il existe

            if next_page_token:
                data["pageToken"] = next_page_token

            # Faire la requête API
            response = requests.post(url, json=data, headers=headers)
            # Traiter la réponse
            if response.status_code == 200:
                results = response.json()
                print(f"Page {page_number} pour '{query}':")
                
                # Sauvegarde des résultats
                safe_banque = banque.replace(" ", "_").replace("(", "").replace(")", "")
                safe_ville = ville.replace(" ", "_")
                filename = f"results_{safe_banque}_{safe_ville}_page_{page_number}.json"
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(results, f, ensure_ascii=False, indent=4)

                # Affichage des infos
                for place in results.get("places", []):
                    print(f"Nom: {place.get('displayName', {}).get('text')}")
                    print(f"Adresse: {place.get('formattedAddress')}")
                    print(f"Note: {place.get('rating')}")
                    print(f"Nombre d'avis: {place.get('userRatingCount')}")
                    print(f"Avis: {place.get('reviews')}")
                    print(f"Adresse courte: {place.get('shortFormattedAddress')}")
                    print("------")
                # Vérifier s'il y a une page suivante
                next_page_token = results.get("nextPageToken")
                if not next_page_token:
                    break

                page_number += 1
                time.sleep(2)
            else:
                print(f"Erreur pour '{query}': {response.status_code}")
                print(response.text)
                break
