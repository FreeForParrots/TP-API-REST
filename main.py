from fastapi import FastAPI

app = FastAPI()

# structure des livres
books = [
    {
    "id": 1,
    "titre": "Le Petit Prince",
    "auteur": "Saint-Exupéry",
    "annee": 1943,
    "categorie": "enfants"
    }
]

# structure des utilisateurs
users = [
    {
    "id": 1,
    "nom": "Alice",
    "email": "alice@test.fr"
    }
]

# page d'accueil
@app.get("/")
def accueil():
    return {"message": "Bienvenue"}

# affichage de toutes les livres
@app.get("/books")
def get_books():
    return books

# affichage de livre par ID
@app.get("/books/{id}")
def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    return {"error": "Livre non trouvé"}

# affichage de livre par titre
@app.get("/books/search/{titre}")
def get_title_book(titre: str):
    for book in books:
        if book["titre"] == titre:
            return book
    return {"error": "Livre non trouvé"}

# affichage de livre par categorie
@app.get("/books/category/{categorie}")
def get_category_book(categorie: str):
    for book in books:
        if book["categorie"] == categorie:
            return book
    return {"error": "Livre non trouvé"}

# ajout de livre
@app.post("/books")
def add_book(book: dict):
    books.append(book)
    return {"message": "Livre ajouté", "book": book}

# modification de livre par ID
@app.put("/books/{id}")
def update_book(id: int, updated_book: dict):
    for i, book in enumerate(books):
        if book["id"] == id:
            books[i] = updated_book
            return {"message": "Livre modifié", "book": updated_book}
    return {"error": "Livre non trouvé"}

# suppretion de livre par ID
@app.delete("/books/{id}")
def delete_book(id: int):
    global books
    books = [b for b in books if b["id"] != id]
    return {"message": "Livre supprimé"}

# affichage de nombre de livres et d'utilisateurs
@app.get("/stats")
def get_stats():
    return {"nbLivres": len(books), "nbUtilisateurs": len(users)}

# création d'utilisateur
@app.post("/users")
def add_user(user: dict):
    users.append(user)
    return {"message": "Utilisateur créé", "user": user}

# connection
@app.post("/login")
def login(credentials: dict):
    login = credentials.get("login")
    password = credentials.get("password")
 
    if login == "admin" and password == "admin":
        return {"token": "123456", "message": "Connexion réussie"}
    return {"error": "Identifiants invalides"}