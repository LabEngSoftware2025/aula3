# Aula 3 - API de gerenciamento de Biblioteca de Livros

Uma API REST para gerenciar livros em um sistema de biblioteca.

## Requisitos
- Python 3.8+
- pip

## Instalação

1. Clone ou extraia os arquivos do projeto
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure variáveis de ambiente (opcional):
   ```bash
   export SECRET_KEY=sua-chave-secreta
   export DATABASE_URL=sqlite:///library.db
   ```

## Executando a Aplicação

```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

## Endpoints da API

### Coleção de Livros
- `GET /api/books` - Listar todos os livros
- `POST /api/books` - Criar um novo livro

### Livro Individual
- `GET /api/books/<id>` - Obter um livro específico
- `PUT /api/books/<id>` - Atualizar um livro
- `DELETE /api/books/<id>` - Excluir um livro

## Exemplos de Requisição/Resposta

### Criar um Livro
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

### Listar Todos os Livros
```bash
curl http://localhost:5000/api/books
```

### Atualizar um Livro
```bash
curl -X PUT http://localhost:5000/api/books/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Dom Casmurro (Atualizado)",
    "pages": 300
  }'
```

### Excluir um Livro
```bash
curl -X DELETE http://localhost:5000/api/books/1
```

## Banco de Dados
Por padrão, utiliza banco de dados SQLite `library.db` no diretório do projeto.Uma API REST para gerenciar livros em um sistema de biblioteca.
