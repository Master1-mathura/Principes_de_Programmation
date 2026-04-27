# TP7 : Architecture Multi-Services avec Docker Compose

Ce TP illustre comment déployer une architecture multi-services (Microservices) à l'aide de Docker Compose. Au lieu de gérer les conteneurs individuellement, nous utilisons un fichier YAML pour orchestrer l'ensemble de l'infrastructure.

## Les avantages de Docker Compose
Docker Compose est l'outil idéal pour lancer des applications nécessitant plusieurs briques (ex: BDD + API + Frontend + Cache). Il permet de :
* **Décrire toute l'architecture** en un seul fichier central : `docker-compose.yml`.
* **Démarrer tout l'environnement** avec une seule commande : `docker compose up`.
* **Automatiser la communication** : les conteneurs communiquent naturellement entre eux via un réseau interne.
* **Versionner et partager** : les configurations sont reproductibles et facilement partageables avec d'autres développeurs.

## Architecture du projet

Le projet est divisé en plusieurs sous-répertoires, chacun représentant un service :

```text
TP7_PP/                      # Vous êtes ici
│
├── docker-compose.yml       # Le "Chef d'Orchestre" (Fichier d'orchestration global)
│
├── product/                 # Service 1 : Backend API (Python)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── api.py
│
└── website/                 # Service 2 : Frontend (PHP)
    └── index.php
```

1.** Le Backend (Service API) : /product**
Ce dossier contient la logique métier de l'application, propulsée par Python.
   - **api.py **: Script utilisant le framework Flask pour créer une API REST qui renvoie une liste de produits au format JSON.
  
   - **requirements.txt** : Liste les dépendances externes (Flask et Flask-RESTful).

   - **Dockerfile** : La recette de création de l'image. Il utilise une image de base Python préconfigurée (python:3-onbuild), copie le code, installe les dépendances et lance le serveur.

2.** Le Frontend (Service Web) : /website**
Ce dossier contient l'interface client.
   - **index.php** : Invoque l'API REST en Python.

   - **DNS interne** : Le fichier PHP utilise file_get_contents('http://product-service/'). Grâce à Docker Compose, le nom du service défini dans le YAML devient son adresse web locale, permettant aux conteneurs de se trouver sans connaître leurs adresses IP.

3. **Le Chef d'Orchestre : docker-compose.yml**
C'est lui qui définit nos deux services (product-service et website). Il gère trois aspects :
   - Le Build & les Images : Il indique à Docker de construire l'image Python à partir du dossier /product et de récupérer une image officielle php:apache pour /website.

   - Les Ports : Il fait le pont entre la machine hôte et les conteneurs (le port 5001 redirige vers l'API, et le 5002 vers le site PHP).

   - Les Volumes : Il lie les dossiers locaux directement à l'intérieur des conteneurs. Si le code est modifié, la mise à jour est immédiate sans avoir à relancer le build.

   - Les Dépendances : L'instruction depends_on garantit que le site PHP (website) ne démarrera que lorsque le backend (product-service) sera lancé, évitant ainsi les erreurs de connexion au démarrage.

## Comment lancer le projet

1. **Démarrer l'architecture**
À la racine du projet (là où se trouve le docker-compose.yml), il faut exécuter :
```bash
docker compose up
```
***Remarque***: *pour lancer en arrière-plan, ajoute l'option -d pour "detach".*

2. **Tester l'application**
Ouvrir le navigateur sur : http://localhost:5002

1. **Gérer l'exécution (Menu interactif)**
Lors d'une exécution classique, un menu interactif est disponible dans le terminal :

- d (Detach) : Bascule le serveur en arrière-plan pour récupérer la main sur le terminal.

- v (View) : Ouvre l'interface graphique de Docker Desktop.

- w (Watch) : Active la surveillance des fichiers pour une mise à jour en temps réel à chaque sauvegarde.

- o (View Config) : Affiche la configuration finale interprétée par Docker.

4. **Tout arrêter**
Si l'application tourne dans le terminal, il faut faire Ctrl + C. Sinon, utiliser :

```bash
docker compose down
```

***Remarque*** *sur le cache des images : Si on modifie des fichiers critiques comme le requirements.txt, l'image existante risque d'être utilisée en cache. Pour forcer Docker Compose à reconstruire les images avec les nouvelles dépendances, il faut à tout prix utiliser :*
```bash
docker compose up --build
```