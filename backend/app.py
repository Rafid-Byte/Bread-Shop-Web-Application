from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/order", methods=["POST"])
def place_order():
    data = request.get_json()
    # Simulasi pemrosesan pesanan
    return jsonify({"message": "Order received", "data": data}), 200

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
