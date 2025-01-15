from flask import Flask, request, jsonify

app = Flask(__name__)

# Liste pour stocker temporairement les données
data_store = []

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.json
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Champs manquants : username ou password"}), 400

    # Ajoute les données reçues au stockage temporaire
    data_store.append({"username": username, "password": password})
    print(f"Données reçues et stockées : {data_store[-1]}")
    return jsonify({"status": "Données reçues avec succès"}), 200

@app.route('/latest', methods=['GET'])
def get_latest_data():
    if not data_store:
        return jsonify({"error": "Aucune donnée disponible"}), 400

    # Renvoie la dernière donnée reçue
    return jsonify(data_store[-1]), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
