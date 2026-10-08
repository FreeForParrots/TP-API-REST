Tests avec cURL

cURL permet de faire des requêtes HTTP directement dans le terminal.
Pour les faire il faut utiliser BASH terminal qui permet les requettes sur plusieurs lignes.



Syntaxe de base
    curl [options] <URL>

Pour les requettes de methode GET la structure est basique
    curl http://localhost:8000/books

    curl http://localhost:8000/books/1


Pour les autres il faut specifier le methode et paramettres si besoin

Exemple d'ajout de livre avec POST
    curl -X POST http://localhost:8000/books \
      -H "Content-Type: application/json" \
      -d '{"id": 3, "titre": "Dune", "auteur": "Frank Herbert"}'

Exemple de modification de livre avec PUT
    curl -X PUT http://localhost:8000/books/1 \
      -H "Content-Type: application/json" \
      -d '{"id": 1, "titre": "Le Petit Prince (édition spéciale)", "auteur": "Saint-Exupéry"}'

Exemple de suppretion ave DELETE
    curl -X DELETE http://localhost:8000/books/2