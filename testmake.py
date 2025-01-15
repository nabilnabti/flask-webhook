import requests

# URL du webhook Make
MAKE_WEBHOOK_URL = "https://hook.eu2.make.com/w7hlrakpspmxce7uj4u6lj57rtuldsfr"

try:
    print("Envoi d'une requête au webhook Make...")
    response = requests.get(MAKE_WEBHOOK_URL)
    print("Statut de la réponse :", response.status_code)
    print("Contenu brut de la réponse :", response.text)
except Exception as e:
    print("Erreur lors de la connexion au webhook :", e)
