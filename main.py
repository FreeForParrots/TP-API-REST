from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

#classe pour livres
class Livre:
    def __init__(self, id, titre, auteur):
        self.id = id
        self.titre = titre
        self.auteur = auteur

    def description(self):
        return f"{self.titre} - {self.auteur}"


# class pour utilisateurs
class Utilisateur:
    def __init__(self, id, nom, email, login):
        self.id = id
        self.nom = nom
        self.email = email
        self.login = login


# 
class BookCreate(BaseModel):
    id: int
    titre: str
    auteur: str


class UserCreate(BaseModel):
    id: int
    nom: str
    email: EmailStr
    login: str
    password: str


# liste des livres
books = [
    {
        "id": 1,
        "titre": "Le Petit Prince",
        "auteur": "Saint-Exupéry",
        "annee": 1943,
        "categorie": "enfants"
    }
]

# liste des utilisateurs
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
    raise HTTPException(status_code=404, detail="Livre non trouvé")

# affichage de livre par titre
@app.get("/books/search/{titre}")
def get_title_book(titre: str):
    for book in books:
        if book["titre"] == titre:
            return book
    raise HTTPException(status_code=404, detail="Livre non trouvé")

# affichage de livre par categorie
@app.get("/books/category/{categorie}")
def get_category_book(categorie: str):
    for book in books:
        if book["categorie"] == categorie:
            return book
    raise HTTPException(status_code=404, detail="Livre non trouvé")

# ajout de livre
@app.post("/books", status_code=201)
def add_book(book: BookCreate):
    books.append(book.model_dump())
    return {"message": "Livre ajouté", "book": book}

# modification de livre par ID
@app.put("/books/{id}")
def update_book(id: int, updated_book: dict):
    for i, book in enumerate(books):
        if book["id"] == id:
            books[i] = updated_book
            return {"message": "Livre modifié", "book": updated_book}
    raise HTTPException(status_code=404, detail="Livre non trouvé")

# suppretion de livre par ID
@app.delete("/books/{id}", status_code=204)
def delete_book(id: int):
    global books
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"message": "Livre supprimé"}
    raise HTTPException(status_code=404, detail="Livre non trouvé")

# affichage de nombre de livres et d'utilisateurs
@app.get("/stats")
def get_stats():
    return {"nbLivres": len(books), "nbUtilisateurs": len(users)}

# création d'utilisateur
@app.post("/users", status_code=201)
def add_user(user: UserCreate):
    users.append(user.model_dump())
    return {"message": "Utilisateur créé", "user": user}

# connection
@app.post("/login")
def login(credentials: dict):
    login = credentials.get("login")
    password = credentials.get("password")
    if login == "admin" and password == "admin":
        return {"token": "123456", "message": "Connexion réussie"}
    raise HTTPException(status_code=401, detail="Identifiants invalides")