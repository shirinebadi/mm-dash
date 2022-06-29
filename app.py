import time
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/api/health_check', methods=['GET'])
def check_health():
    return jsonify({
        'message': 'OK'
    }), 200

@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html') 


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8000)