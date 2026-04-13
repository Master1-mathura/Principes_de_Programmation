# TP7 : Multi-Services avec Docker Compose

Ce TP illustre comment déployer une architecture multi-services (Microservices) à l'aide de Docker Compose. Au lieu de gérer les conteneurs individuellement, nous utilisons un fichier YAML pour décrire l'ensemble de l'infrastructure.

**Docker Compose :** Outil permettant de décrire toute l'architecture dans un fichier `docker-compose.yml`. Une seule commande démarre tout.

**DNS Interne :** Les conteneurs communiquent automatiquement entre eux en utilisant leur nom de service (ex: le PHP appelle l'API via `http://product-service/`).

**Dépendances :** L'instruction `depends_on` garantit que le site PHP ne démarrera que lorsque l'API Python sera prête.

* Service Web - Frontend
Dans le dossier /website
Dans le dossier website, crée un seul fichier nommé index.php.
Ce fichier utilise file_get_contents('http://product-service/') pour interroger l'API. C'est la magie de Docker : le nom du service devient son adresse web locale.

* Service API - Backend
Dans le dossier /product.
Ce dossier contient la logique métier de l'application répartie en trois fichiers :

- api.py : Le script Python utilisant le framework Flask pour créer une API REST qui renvoie simplement une liste de produits au format JSON.
- requirements.txt : Un fichier listant les bibliothèques externes nécessaires (Flask et Flask-RESTful) pour que Docker sache quoi installer.
- Dockerfile (la recette de création de l'image) : Il utilise une image Python préconfigurée (3-onbuild) qui copie automatiquement le code, installe les dépendances listées, et lance le serveur.

* Le Chef d'Orchestre
Dans le fichier `docker-compose.yml` à la racine du TP7.
C'est le fichier central qui définit les deux services (product-service et website) et gère trois aspects cruciaux :

- **Le Build & les Images** : Il dit à Docker de construire l'image Python à partir du dossier product et de télécharger une image PHP/Apache officielle pour le dossier website.
- **Les Ports** : Il fait le pont entre ton Mac et les conteneurs (ex: le port 5001 de ton ordinateur redirige vers l'API, et le 5002 vers le site PHP)
- **Les Volumes** : Il lie tes dossiers locaux directement à l'intérieur des conteneurs. Ainsi, si tu modifies ton code, la mise à jour est immédiate sans avoir à tout reconstruire.

Maintenant, il ne reste plus qu'à :
1) Démarrer l'architecture : `docker compose up` (ou docker compose up -d pour l'arrière-plan) -> ça peut prendre un moment.

Le menu (v, o, w, d) apparait : 
- d (Detach) : le serveur va continuer à tourner silencieusement en arrière-plan.

- v (View) : Ouvre l'interface graphique de Docker Desktop pour voir les conteneurs avec la souris.

- w (Watch) : Active un mode où Docker surveille les fichiers et met à jour le conteneur en temps réel à chaque sauvegarde.

- o (View Config) : Affiche le fichier de configuration final que Docker a compris.

*Il faut appuyer simplement sur d pour récupérer la main sur le terminal*

2) Vérifier le résultat : Ouvrir le navigateur sur http://localhost:5002.
3) Arrêter tout : Ctrl + C puis docker compose down.

On a ainsi l'arborescence suivante :
```text
TP7_PP/
│
├── docker-compose.yml       # Fichier d'orchestration global
│
├── product/                 # Service 1 : Backend API (Python)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── api.py
│
└── website/                 # Service 2 : Frontend (PHP)
    └── index.php
```

Remarque :
A la suite d'une erreur dans requirements.txt, j'ai modifié les dépendances, donc j'ai dû dire à Docker Compose de forcer la reconstruction de l'image (sinon il risque de reprendre l'ancienne version buggée en mémoire) :
`docker compose up --build`.