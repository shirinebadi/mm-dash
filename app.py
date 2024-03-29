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

@app.route('/movies/<int:id>')
def idsearch(id):
    movie = Movie.query.filter_by(id = id).first()
    movie.id = str(movie.id)
    if movie.id == '1' or movie.id == '2':
        return render_template('movie12.html', movie=movie)
    else:
        html_file = 'movie' + movie.id + '.html'
        return render_template(html_file, movie=movie)


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    m = Movie()
    movie1 = Movie(title = "The Shawshank Redemption", info = "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",star = 9.3,director =  "Frank Darabont")
   
    movie2 = Movie(title = "The Godfather",info = "The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.", star = 9.2,director =  "Francis Ford Coppola" )
    movie3 = Movie(title =  "The Dark Knight", info = "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",star = 9.0, director = "Christopher Nolan")
    movie4 = Movie(title =  "The Godfather Part II ", info = "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.", star = 9.0, director = "Francis Ford Coppola" )
    movie5 = Movie(title = "12 Angry Men ", info = "The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.", star = 8.9, director ="Sidney Lumet" )
    movie6 = Movie(title = "Schindler's List",info =  "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.", star = 9.0, director = " Steven Spielberg" )

    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.add(movie4)
    db.session.add(movie5)
    db.session.add(movie6)
    db.session.commit()
    app.run(host= '0.0.0.0', port=8000)