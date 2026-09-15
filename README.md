# TP Docker

**Étudiant :** Julien BRAS  
**Formation :** M2 MIAGE IPM  
**Université :** Université Toulouse Capitole

## Travail réalisé

- Création d'une application web minimale avec Flask.
- Ajout d'une route `/` qui écrit un objet dans MongoDB, le relit immédiatement, puis affiche sa valeur.
- Création d'un `Dockerfile` basé sur Python 3.9.
- Installation de Flask et PyMongo avec `requirements.txt`.
- Configuration du conteneur pour utiliser le port 5000.
- Ajout d'une base MongoDB accessible sur le port standard 27017.

## Lancer l'application

Lancer Flask et MongoDB avec Docker Compose :

```bash
docker compose up -d
```

L'application est ensuite accessible à l'adresse suivante :

<http://localhost:5000>

À chaque requête sur `/`, l'application écrit un objet dans MongoDB, le relit immédiatement, puis affiche sa valeur.

## Fichiers

- `app.py` : application Flask.
- `Dockerfile` : configuration de l'image Docker.
- `requirements.txt` : dépendances Python.
- `docker-compose.yml` : docker compose des conteneurs de l'application Flask ainsi que de la base de données Mongo.
