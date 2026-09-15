# TP Docker

**Étudiant :** Julien BRAS  
**Formation :** M2 MIAGE IPM  
**Université :** Université Toulouse Capitole

## Travail réalisé

- Création d'une application web minimale avec Flask.
- Ajout d'une route `/` qui affiche « Hello, World! ».
- Création d'un `Dockerfile` basé sur Python 3.9.
- Installation de Flask avec `requirements.txt`.
- Configuration du conteneur pour utiliser le port 5000.

## Lancer l'application

Construire l'image Docker :

```bash
docker build -t flask-app .
```

Lancer le conteneur :

```bash
docker run -p 5000:5000 flask-app
```

L'application est ensuite accessible à l'adresse suivante :

<http://localhost:5000>

## Fichiers

- `app.py` : application Flask.
- `Dockerfile` : configuration de l'image Docker.
- `requirements.txt` : dépendances Python.
