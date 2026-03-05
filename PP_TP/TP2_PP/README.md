Pour ce TP2, nous allons reprendre le serveur du TP0 (serveur_student) mais changer de client. Dans le TP0, le serveur Flask/Python parlait avec un client Request/Python, dans ce TP2, le serveur Flask/Python, va parler avec un client PHP :

Le client fait une requête HTTP au serveur Python, reçoit en réponse le JSON et le décode pour en prendre les données et en fait une page HTML lisible par l'utilisateur.

# Exercice 1 : Connexion à l'API, affichage du texte brut

Les données envoyées par le serveur Python sont au format JSON (une longue chaîne de caractères). PHP ne peut pas manipuler ces données directement comme s'il s'agissait de variables classiques.

# Exercice 2 : Traitement des données

Utilisation de `file_get_contents($url)` pour récupérer le contenu de l'API, puis de `json_decode($response, true)` pour transformer cette chaîne en un tableau associatif que l'on pourra donc parcourir comme on veut, car chaque élément du tableau a une clé spécifique. Avec cette clé, on peut afficher/extraire les informations que l'on souhaite dans l'ordre que l'on souhaite.

# Exercice 3 : Automatisation de l'affichage

Une fois le tableau récupéré, il contient une liste complète d'étudiants. Il faut pouvoir accéder aux informations de chaque étudiant individuellement pour les traiter. Donc dans l'exo3, on met en place une boucle foreach (`$students as $student`) pour parcourir le tableau et extraire les clés spécifiques comme ['name'] (ou ['prenom']) et ['age'].

# Exercice 4 : Centralisation de la Configuration

Dans les exercices précédents, l'URL de l'API Flask (`http://127.0.0.1:5000/students`) était écrite en haut de chaque fichier PHP. 
Donc si notre serveur Python venait à changer de port, il faudrait ouvrir et modifier manuellement chaque fichier PHP.
Pour corriger cela, nous devons respecter un principe fondamental en développement : **ne jamais mélanger la logique métier et la configuration**.

* **La Configuration :** Ce sont les variables liées à l'environnement d'exécution (serveurs, adresses IP, ports, mots de passe). Ici, c'est l'URL d'accès à l'API (`$url ="http://127.0.0.1:5000/students";`).
* **La Logique Métier :** C'est le fait d'appeler l'API, de décoder le JSON (`json_decode`) et d'afficher le résultat pour l'utilisateur (`foreach`). Cette logique ne change jamais, quelle que soit l'adresse du serveur.

Dans l'exo4, on a donc restructuré le projet comme suit :

1. Création d'un dossier `config/` contenant un fichier `config.php`.
2. Déclaration d'une constante globale dans ce fichier contenant notre URL.
3. Appel de ce fichier de configuration au début de notre script principal (`exo4.php`) via `require_once`.

Maintenant, si l'URL de l'API change, nous n'aurons plus qu'un seul et unique fichier à modifier (`config.php`), et l'ensemble de notre projet se mettra à jour automatiquement.

# Exercice 5 : Création d'un "Service"

Pour l'instant, notre fichier principal faisait encore trop de choses à la fois. Dans l'exo5, on introduit donc la notion de "Service" pour séparer la logique d'accès aux données (interroger l'API avec `file_get_contents` et traduire le JSON en tableau PHP avec `json_decode`) de l'affichage (générer le code HTML et boucler sur les données avec `foreach` pour les montrer à l'utilisateur).

* **Le Service :** C'est un fichier dédié (une Classe PHP) dont l'unique rôle est de communiquer avec l'API. Il récupère les données brutes et les retourne. Il ne contient **aucun** affichage (aucun `echo`, aucune balise HTML).
* **Le Script Principal :** Il se contente d'appeler le Service pour obtenir les données prêtes à l'emploi, puis s'occupe de la boucle `foreach` pour générer le rendu HTML.

Dans l'exo5, on a donc restructuré le projet comme suit :

1. **Création d'un répertoire `services/` :** Ce dossier regroupe nos classes métiers.
2. **Création de la classe `StudentService` :** Dans ce dossier, nous avons créé le fichier `StudentService.php` contenant une fonction publique et statique `getAllStudents()`. Cette fonction utilise notre constante `API_BASE_URL` (définie dans la config), effectue l'appel à l'API et retourne le tableau décodé.
3. **Mise à jour du script principal (`exo5.php`) :** Le script principal est maintenant allégé. Il charge la configuration et le service, récupère la liste via `StudentService::getAllStudents()`, et se concentre uniquement sur son affichage final.

Ainsi, si l'API change, on ne modifie que le Service. Si le design HTML change, on ne modifie que le script principal.

# Exercice 6 : Séparation de la Vue

Dans l'exo5, bien que la donnée soit récupérée par le Service, le script principal contenait encore des balises HTML (les `<h3>`, les `<br>`) et des `echo`.
Donc si on veut modifier le design de la page, on est obligé de fouiller au milieu du code PHP et modifier.
Ainsi, pour obtenir un code "propre", lisible et facile à faire évoluer, nous avons appliqué le principe suivant : le contrôleur (`exo6.php`) prépare les données (il charge la configuration, demande les données au Service, les stocke dans une variable, puis appelle la Vue pour lui passer le relais) et la vue s'occupe uniquement de l'affichage (`views/students.php`) (pas d'appel d'API, pas de logique métier uniquement du HTML et des balises PHP minimales pour afficher les données préalablement préparées par le contrôleur)

Dans l'exo6, on a donc restructuré le projet comme suit :

1. **Création du répertoire `views/` :** Ce dossier contient tous les fichiers d'interface de notre application.
2. **Création de la vue `students.php` :** Nous avons créé ce fichier dans le dossier `views/`. Il contient le HTML structuré (titres, listes) et boucle sur la variable `$students`.
3. **Mise à jour du script principal (`exo6.php`) :** Les lignes de code contenant des `echo` ont été totalement supprimées. À la place, le script se termine simplement par un `require_once 'views/students.php';`.

# Exercice 7 : Finalisation de l'Interface (HTML5 & CSS3)
On a les trois couches du web :
1. **PHP (Le fond)** : fournit les données grâce au Service.
2. **HTML (La structure)** : organise le contenu de manière sémantique (`DOCTYPE`, `head`, `body`).
3. **CSS (La forme)** : embellit l'interface pour la rendre agréable à l'utilisateur.

Dans l'exo7, on a donc restructuré le projet comme suit :

* **Création du répertoire `assets/style.css`** : contient toutes les règles de mise en forme (couleurs, polices, marges). Il apporte les modifications suivantes : 1) **Corps de page (`body`)** : Utilisation d'une police sans-serif (Arial), fond gris clair (`#f5f5f5`) et ajout de padding pour aérer le contenu. 2) **Conteneur de liste (`ul`)** : Transformation en bloc blanc avec des coins arrondis (`border-radius`), une largeur fixe de `300px` et une ombre légère pour créer du relief. 3) **Éléments de liste (`li`)** : Ajout d'espacement entre les étudiants pour une meilleure lisibilité.


* **`views/students.php`** : A été mis à jour pour devenir un document HTML5 complet incluant le lien vers la feuille de style.