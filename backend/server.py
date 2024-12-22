from flask import Flask, jsonify
from flask_cors import CORS
from main import analyze_crypto_asset

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/crypto-asset/<crypto_asset_name>', methods=['GET'])
def get_crypto_asset_analysis(crypto_asset_name):
    result = analyze_crypto_asset(crypto_asset_name)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)