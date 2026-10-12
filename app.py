import os

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Secure DevSecOps Demo App"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=False, host=os.environ.get('HOST', '127.0.0.1'), port=5000)