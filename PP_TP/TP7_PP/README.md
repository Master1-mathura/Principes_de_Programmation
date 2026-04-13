# TP7 : Multi-Services avec Docker Compose

Ce TP illustre comment déployer une architecture multi-services (Microservices) à l'aide de Docker Compose. Au lieu de gérer les conteneurs individuellement, nous utilisons un fichier YAML pour décrire l'ensemble de l'infrastructure.

**Docker Compose :** Outil permettant de décrire toute l'architecture dans un fichier `docker-compose.yml`. Une seule commande démarre tout.

**DNS Interne :** Les conteneurs communiquent automatiquement entre eux en utilisant leur nom de service (ex: le PHP appelle l'API via `http://product-service/`).

**Dépendances :** L'instruction `depends_on` garantit que le site PHP ne démarrera que lorsque l'API Python sera prête.

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