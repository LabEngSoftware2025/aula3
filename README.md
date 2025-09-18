# Aula 3
Criem uma aplicação que permite cadastrar, editar, remover e listar livros para uma biblioteca. Um livro tem um título, autor(as/es), quantidade de páginas e ano de publicação. A aplicação deve ser acessível e manipulável por API REST e os dados devem ser salvos em um banco de dados. Indiquem as URLs para acesso às funcionalidades.


# Library Book Management API

A REST API for managing books in a library system.

## Requirements
- Python 3.8+
- pip

## Installation

1. Clone or extract the project files
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set environment variables (optional):
   ```bash
   export SECRET_KEY=your-secret-key
   export DATABASE_URL=sqlite:///library.db
   ```

## Running the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Books Collection
- `GET /api/books` - List all books
- `POST /api/books` - Create a new book

### Single Book
- `GET /api/books/<id>` - Get a specific book
- `PUT /api/books/<id>` - Update a book
- `DELETE /api/books/<id>` - Delete a book

## Request/Response Examples

### Create a Book
```bash
curl -X POST http://localhost:5000/api/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Dom Casmurro",
    "author": "Machado de Assis",
    "pages": 256,
    "year": 1899
  }'
```

### List All Books
```bash
curl http://localhost:5000/api/books
```

### Update a Book
```bash
curl -X PUT http://localhost:5000/api/books/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Dom Casmurro (Updated)",
    "pages": 300
  }'
```

### Delete a Book
```bash
curl -X DELETE http://localhost:5000/api/books/1
```

## Database
By default, uses SQLite database `library.db` in the project directory.