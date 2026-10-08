#!/bin/bash

echo "=== Test API Bibliothèque ==="

echo "\n1. Récupérer tous les livres"
curl http://localhost:8000/books | python -m json.tool

echo "\n2. Récupérer le livre 1"
curl http://localhost:8000/books/1 | python -m json.tool

echo "\n3. Ajouter un livre"
curl -X POST http://localhost:8000/books \
    -H "Content-Type: application/json" \
    -d '{"id": 3, "titre": "Dune", "auteur": "Frank Herbert"}' | python -m json.tool

echo "\n4. Se connecter"
curl -X POST http://localhost:8000/login \
    -H "Content-Type: application/json" \
    -d '{"login": "admin", "password": "admin"}' | python -m json.tool

echo "\n=== Tests terminés ==="
