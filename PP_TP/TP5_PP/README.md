## Création du fichier Dockerfile :

Nous avons conteneurisé l'API du TP2 avec un Dockerfile et on l'a fait tourner de manière isolée.

### L'API est empaquetée avec les instructions suivantes :
1) Définition du dossier de travail dans le conteneur
2) Installation du framework Flask
3) Copie de tous les fichiers locaux vers le conteneur
4) Documentation le port utilisé par notre application
5) Commande de démarrage

### Commandes de Lancement :

Construire l'image :
```bash
docker build -t mon-app-tp2 .
```

Démarrage du conteneur (mapping du port 4900 du Mac vers le port 5000 du conteneur) :

```bash
docker run -p 4900:5000 mon-app-tp2
```

Test de l'API : Ouvrir le navigateur à l'adresse http://localhost:4900.
Attention : On doit forcer l'écoute avec app.run(host='0.0.0.0', port=5000) dans serveur_student.py