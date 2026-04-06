# Suivi des commandes utilisées durant le TP sur les Dockers
Ce fichier contient toutes les commandes exécutées lors du TP.

## Tests de base
- Lancement image test : `docker run hello-world`
- Test mode interactif : `docker run -it alpine:latest /bin/sh`

On lance la commande `docker build -t mon-alpine-custom .` pour :
- docker build : construire une nouvelle image à partir des instructions contenues dans un fichier nommé Dockerfile
- -t mon-alpine-custom : "Tag" (étiquette) -> on le nomme mon-alpine-custom
- . : le dossier courant

Maintenant qu'elle est créée on vérifie qu'elle fonctionne en rentrant dedans avec :
`docker run -it mon-alpine-custom`

`curl http://google.com` permet de demander à google de renvoyer la page http://google.com

## Nginx, Ports et Bind Mounts
Puis on va lancer un serveur web et lier un fichier de mon pc directement à l'intérieur du conteneur : on crée la page index.html, on lance le serveur Nginx en connectant le volume avec la commande :
`docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html --name monServeurWeb nginx`

On va sur http://localhost:8080 pour voir le résultat.