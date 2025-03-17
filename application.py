from flask import Flask, jsonify
from flask_cors import CORS

application = Flask(__name__)  # Changed from app to application
CORS(application)

@application.route('/')
def home():
    return jsonify(message="Hello from Flask!")

@application.route('/status/')
def status():
    return jsonify(status="Backend is running")
@application.route('/status/${id}')
def status():
    return jsonify(status="Backend is running")

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
