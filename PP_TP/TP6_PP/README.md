# TP6 : Publication sur Docker Hub

Ce TP se concentre sur le partage d'images Docker via **Docker Hub**.

## 1. Création d'une Image Basique (Alpine)

Pour tester la publication, nous utilisons l'image Linux la plus légère possible (`alpine`) pour afficher un simple message.

Cycle complet pour créer et envoyer une image en ligne pour qu'elle soit accessible publiquement :

1) Construire l'image localement : `docker build -t mon-app .`
2) Tester l'image en local : `docker run mon-app` *Résultat attendu : Bonjour à toi*
3) Se connecter à Docker Hub depuis le terminal : `docker login`
4) Créer un Tag (il faut renommer l'image avec son nom d'utilisateur Docker Hub exact) : `docker tag mon-app mathurasanthalingam/mon-app:1`
5) Pousser l'image sur les serveurs de Docker : `docker push mathurasanthalingam/mon-app:1`

Une fois publiée, n'importe qui peut récupérer et lancer l'image avec la commande : `docker run username/mon-app:1`

Attention : Si l'image a été compilée sur un processeur différent (ex: création sur un Windows, exécution sur un Mac), Docker affichera une erreur de "manifest", il faut "forcer l'émulation" avec le flag `--platform` : `docker run --platform linux/amd64 mathurinmartel/mathurin_mon_message:1`
