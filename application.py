from flask import Flask, jsonify
from flask_cors import CORS

application = Flask(__name__)  # Changed from app to application for Elastic Beanstalk compatibility
CORS(application)

@application.route('/')
def home():
    return jsonify(message="Hello from Flask!")

@application.route('/status/')
def status():
    return jsonify(status="Backend is running")

@application.route('/completed/')
def completed():
    return jsonify(status="Backend is completed")

@application.route('/test/')
def test():
    return jsonify(status="Backend is test")

@application.route('/status/<id>')
def status_with_id(id):
    return jsonify(status=f"Backend is running for ID: {id}")

@application.route('/items/')
def items():
    # Returning a list of items
    return jsonify(items=["item1", "item2", "item3"])

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=80)  # Ensure this runs on port 80 for Elastic Beanstalk
