Pour ce TP3, nous passons d'une lecture de fichiers (comme au TP2) à une architecture interconnectée avec une base de données relationnelle.

Pour ce faire, nous avons installé le **moteur, un serveur MySQL** qui tourne en arrière-plan sur l'ordinateur. Son rôle est de stocker, sécuriser et requêter les données. Et nous avons installé le **client, une extension VS Code "Database Client"** qui sert en quelques sortes de "pont" visuel pour se connecter au moteur et exécuter nos commandes SQL.

Nous avons ainsi créé au préalable la base `school_api` et la table `students`.

Nous avons ensuité créé 4 fichiers :

1. `config.py` : contient les clés pour ouvrir la base de données. Ce fichier permet d'éviter une connexion globale. En effet, quand on écrit conn = mysql.connector.connect(...) tout en haut du fichier app.py, on établit une connexion globale qui est exécutée une seule fois au démarrage du serveur Python. Cette connexion unique reste stockée dans la mémoire vive de l'ordinateur. Si plusieurs utilisateurs visitent l'API en même temps, ils utilisent tous cette même connexion. Grâce au fichier config.py, on peut créer une fonction `get_connection()` dans `db.py`. Cela permet de recréer une connexion propre et indépendante à chaque nouvelle requête HTTP.

2. `db.py` : utilise la configuration pour ouvrir concrètement le "tuyau" vers MySQL.

3. `repository.py` (c'est le DAO): c'est ici que l'on place nos requêtes SQL. Ce fichier demande la connexion, va chercher les étudiants dans la table, et transforme le résultat en dictionnaire grâce à `dictionary=True`.

4. `app.py` : utilise le framework Flask et crée les "routes" (les URL) que l'on pourra visiter sur le navigateur.


Une fois ces fichiers créés et configurés, nous avons lancé le serveur Flask via le terminal avec la commande `python3 app.py`. 
Le serveur écoute les requêtes sur le port local `5001`. Selon les routes définies, on obtient différents affichages :

* **Sur la racine** (http://localhost:5001/) : Le navigateur affiche le texte brut `"C'est cool REST !"`. Donc le serveur web Flask fonctionne et écoute nos requêtes.
* **Sur la route des étudiants** (http://localhost:5001/students) : Le navigateur affiche `[]`. Il s'agit d'un tableau JSON vide. Voici ce qu'il se passe concrètement :
  1. `app.py` a reçu la requête HTTP GET.
  2. Il a appelé la fonction de `repository.py`.
  3. Le repository a utilisé `db.py` et `config.py` pour ouvrir une connexion à MySQL.
  4. La requête `SELECT * FROM students` a été exécutée.
  5. Le résultat (vide, car nous n'avons pas encore inséré de données) a été renvoyé et transformé en format JSON pour le navigateur.

Ceci étant fait, nous avons ajouté des fonctions pour compléter notre système avec les opérations classiques : recherche par id, ajout, suppression et modification. Nous les avons intégrés dans le fichier `repository.py` avec notamment des `conn.commit()` pour valider l'enregistrement.

Enfin, nous avons créé un script `test.py` pour simuler l'ajout, la modification et la suppression d'un étudiant. Cela nous a permis de vérifier que la communication avec MySQL est bien fonctionnelle.

# Pour aller plus loin : conteneurisation

Un conteneur Docker est comme un ordinateur complètement vierge et isolé donc on peut rencontrer le problème de la connexion locale :
Si l'API cherche à se connecter à une base MySQL qui tourne sur le Mac (via localhost), elle plantera. Pour le conteneur, localhost désigne l'intérieur de sa propre boîte, il n'y trouvera donc pas le serveur MySQL du Mac.

Pour cela, il faut explicitement dire au conteneur d'installer les outils de communication avec la base de données dans le Dockerfile :

`RUN pip install flask mysql-connector-python`

La vraie solution reste néanmoins le Docker Compose pour lancer l'API et la base de données ensemble et les relier proprement.