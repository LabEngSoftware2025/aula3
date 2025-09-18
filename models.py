from database import db

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'pages': self.pages,
            'year': self.year
        }
    
    def __repr__(self):
        return f'<Book {self.title}>'