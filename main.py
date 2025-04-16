import logging
import os
from flask import Flask, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def root():
    logger.info("Root endpoint was called")
    return jsonify({"message": "Hello World from Flask"})

@app.route('/env_var_message')
def env_var_message():
    logger.info("env_var_message endpoint was called")
    message = os.getenv('MESSAGE', 'No message set')
    return jsonify({"message": message})

@app.route('/env_var_number')
def env_var_number():
    logger.info("env_var_number endpoint was called")
    number = os.getenv('NUMBER', '0')
    return jsonify({"number": number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8000)), debug=True)
