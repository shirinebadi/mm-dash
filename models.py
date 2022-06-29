from app import db

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text) 
    star = db.Column(db.SmallInteger)
    director = db.Column(db.String(255)) 

    def __repr__(self):
        return "<Movie %r>" % self.title

if __name__ == "__main__":
    db.create_all()