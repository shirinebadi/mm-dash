import time
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.route('/api/health_check', methods=['GET'])
def check_health():
    return jsonify({
        'message': 'OK'
    }), 200

@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')

@app.route('/api/<int:id>')
def search_by_id():
    pass


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8000)