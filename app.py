import requests
from playwright.sync_api import sync_playwright

# URL pour récupérer les dernières données
LATEST_URL = "https://flask-webhook-4u0c.onrender.com/latest"

def get_latest_data():
    """
    Récupère les dernières données depuis Render via l'endpoint /latest.
    """
    try:
        response = requests.get(LATEST_URL)
        if response.status_code == 200:
            data = response.json()
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                raise ValueError("Les champs 'username' ou 'password' sont manquants dans la réponse.")

            return username, password
        else:
            print(f"Erreur lors de la requête : {response.status_code}, {response.text}")
            return None, None
    except Exception as e:
        print(f"Erreur de connexion à Render : {e}")
        return None, None

def perform_browser_actions(username, password):
    """
    Ouvre le navigateur et effectue les actions en utilisant les données récupérées.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("Accès à la page d'accueil...")
        page.goto("https://autoentrepreneur.urssaf.fr/")

        print("Clique sur le bouton 'Se connecter'...")
        page.click("a#link_mon_compte_deconnecte")

        print("Remplissage des champs de connexion...")
        page.fill("input#compte_id", username)
        page.fill("input#compte_mdp", password)

        print("Soumission du formulaire...")
        page.click("button[type='submit']")

        print("Navigation terminée.")
        input("Appuie sur Entrée pour fermer le navigateur...")
        browser.close()

# Étape 1 : Récupère les données depuis /latest
username, password = get_latest_data()

if username and password:
    perform_browser_actions(username, password)
else:
    print("Impossible de récupérer les données. Vérifie l'endpoint /latest.")
