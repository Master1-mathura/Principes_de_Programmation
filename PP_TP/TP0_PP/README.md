Pour ce premier TP, nous avons développé deux serveurs API :
- la gestion d'étudiants
- la gestion des suspects dans un scénario de meurtre

Définitions à connaître : Endpoint (= là où l'API reçoit une requête et renvoie une réponse)
dépendances (installation de codes pré-existants pour ne pas avoir à les réécrire soi-même)

L'exécution des serveurs rend accessible l'API à l'adresse locale : http://127.0.0.1:5000/
Puis, dans les deux API, nous avons implémenté les Endpoints :
- **GET** avec /suspects : pour récupérer la liste complète des informations concernant tous les suspects
- **GET** avec /suspects/<id> : pour récupérer les informations concernant un suspect via son <id>
- **POST** avec /suspects : pour créer et ajouter un nouveau suspect à la liste
- **PUT** avec /suspects/<id> : pour modifier les informations concernant un suspect via son <id>
- **DELETE** avec /suspects/<id> : pour supprimer de la liste un suspect via son <id>
N.B : <id> est unique.

Pour cela, nous avons installé les dépendances
- **flask** pour créer le serveur web, gérer les routes et les réponses JSON
- **requests** pour simuler un clien et envoyer des requetes HTTP au serveur

Nous avons effectué et vérifié chaque méthode de deux manières :
- par l'outil **Postman** : on choisit la méthode, on entre l'URL de notre serveur,
via l'onglet Body on envoie nos données
(en sélectionnant le format JSON)
- par l'implémentation de **clients python** (via la bibliothèque requests) : communication directe avec l'URL locale

Remarques :
- lors de l'exécution du serveur des suspects, nous avons remarqué que Flask triait dans l'ordre
alphabétique les clés du JSON, c'est pourquoi on a ajouté **app.json.sort_keys = False** dans l'application flask
pour conserver l'ordre original et assuré plus de cohérence.

- concernant **GET** ou **PUT**, nous avons remarqué que si deux individus avaient un même
id, GET (et notamment PUT) ne prenant en considération que le premier des deux.
Cela est dû au fait que **next()** s'arrête dès qu'il trouve une correspondance trouvée

- **Gitignore** : lors de la synchronisation du dossier avec Gitlab, nous avons ignoré les fichiers lourds comme .venv et .idea
en les ajoutant dans le fichier .gitignore