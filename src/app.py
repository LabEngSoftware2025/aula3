from flask import Flask, request, jsonify
from aula3.service.database import db
from models import Book
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

# API Routes

@app.route('/api/books', methods=['GET'])
def get_books():
    """List all books"""
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """Get a specific book by ID"""
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

@app.route('/api/books', methods=['POST'])
def create_book():
    """Create a new book"""
    data = request.get_json()
    
    if not all(key in data for key in ['title', 'author', 'pages', 'year']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    book = Book(
        title=data['title'],
        author=data['author'],
        pages=data['pages'],
        year=data['year']
    )
    
    db.session.add(book)
    db.session.commit()
    
    return jsonify(book.to_dict()), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """Update an existing book"""
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    
    if 'title' in data:
        book.title = data['title']
    if 'author' in data:
        book.author = data['author']
    if 'pages' in data:
        book.pages = data['pages']
    if 'year' in data:
        book.year = data['year']
    
    db.session.commit()
    
    return jsonify(book.to_dict())

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Delete a book"""
    book = Book.query.get_or_404(book_id)
    
    db.session.delete(book)
    db.session.commit()
    
    return jsonify({'message': 'Book deleted successfully'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)