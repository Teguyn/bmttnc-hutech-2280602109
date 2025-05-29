from flask import Flask, request, jsonify
from cipher.PlayFair import PlayfairCipher

app = Flask(__name__)

# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayfairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_create_matrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    key = data['key']
    plain_text = data['plain_text']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({"encrypted_text": encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    key = data['key']
    cipher_text = data['cipher_text']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({"decrypted_text": decrypted_text})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    