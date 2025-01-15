from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.json
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Champs manquants : username ou password"}), 400

    print(f"Username : {username}, Password : {password}")
    return jsonify({"status": "Données reçues avec succès"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
