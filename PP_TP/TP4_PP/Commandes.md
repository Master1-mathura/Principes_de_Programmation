# Suivi des commandes utilisées durant le TP sur les Dockers
Ce fichier contient toutes les commandes exécutées lors du TP.

## 1. Tests de base
- Lancement image test : `docker run hello-world`
- Test mode interactif : `docker run -it alpine:latest /bin/sh`

On lance la commande `docker build -t mon-alpine-custom .` pour :
- docker build : construire une nouvelle image à partir des instructions contenues dans un fichier nommé Dockerfile
- -t mon-alpine-custom : "Tag" (étiquette) -> on le nomme mon-alpine-custom
- . : le dossier courant

Maintenant qu'elle est créée on vérifie qu'elle fonctionne en rentrant dedans avec :
`docker run -it mon-alpine-custom`

`curl http://google.com` permet de demander à google de renvoyer la page http://google.com

