import requests
from playwright.sync_api import sync_playwright

# URL du webhook Make
MAKE_WEBHOOK_URL = "https://hook.eu2.make.com/w7hlrakpspmxce7uj4u6lj57rtuldsfr"

def get_credentials_from_make():
    """
    Récupère les informations envoyées au webhook Make.
    """
    try:
        print("Envoi d'une requête au webhook Make...")
        response = requests.get(MAKE_WEBHOOK_URL)
        response.raise_for_status()

        # Récupérer les données au format JSON
        data = response.json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise ValueError("Données manquantes : username ou password.")

        print(f"Informations récupérées : Email={username}, Mot de passe=[protégé]")
        return username, password
    except Exception as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return None, None

def test_autoentrepreneur_login(username, password):
    """
    Automatisation de la connexion sur le site URSSAF avec Playwright.
    """
    if not username or not password:
        print("Email ou mot de passe non fourni. Arrêt du script.")
        return

    print("Démarrage de la session Playwright...")
    with sync_playwright() as p:
        # Lancer le navigateur
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()

        # Étape 1 : Accéder à la page d'accueil
        print("Accès à la page d'accueil de l'URSSAF...")
        page.goto("https://www.autoentrepreneur.urssaf.fr/portail/accueil.html")

        # Étape 2 : Cliquer sur "Se connecter"
        print("Navigation vers la page de connexion...")
        page.click("a#link_mon_compte_deconnecte")

        # Étape 3 : Remplir le formulaire de connexion
        print("Remplissage du formulaire...")
        page.fill("input#compte_id", username)
        page.fill("input#compte_mdp", password)

        # Étape 4 : Cliquer sur le bouton "Me connecter"
        print("Validation du formulaire...")
        page.click("form#identification button[type='submit']")

        # Pause pour observer
        page.wait_for_timeout(5000)

        # Fermer le navigateur
        print("Fermeture du navigateur...")
        browser.close()

if __name__ == "__main__":
    # Récupérer les informations depuis Make
    email, password = get_credentials_from_make()

    # Lancer la navigation avec Playwright
    test_autoentrepreneur_login(email, password)
