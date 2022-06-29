import time
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = 'static/images/'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text) 
    star = db.Column(db.Float)
    director = db.Column(db.String(255)) 

    def __repr__(self):
        return "<Movie %r>" % self.title


@app.route('/api/health_check', methods=['GET'])
def check_health():
    return jsonify({
        'message': 'OK'
    }), 200

@app.route('/', methods=['GET'])
def main_page():
    movies = Movie.query.all()
    for movie in movies:
        movie.id = str(movie.id)
    return render_template('index.html', movies = movies)

@app.route('/api/<int:id>')
def search_by_id():
    pass


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8000)