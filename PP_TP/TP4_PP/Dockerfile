# J'ai décidé de retracer l'ensemble du TP dans un Dockerfile.
# On part de l'image officielle Alpine
FROM alpine:latest
# On installe curl pendant la construction
RUN apk add --no-cache curl

# J'ajoute la commande par défaut au lancement pour éviter d'avoir à tout réécrire
CMD ["/bin/sh"]