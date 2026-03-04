<?php
# On cible l'API Flask de port 5000 (comme précisé dans le serveur) :
$url = "http://127.0.0.1:5000/students";

# On récupère le contenu :
$response = file_get_contents($url);

# On désérialise le contenu :
$students = json_decode($response, true);

echo "<pre>";
echo"<h3>Réponse décodée du serveur Python :</h3>";
print_r($students);
# À la place de tout afficher, maintenant que tout est sous la forme d'un tableau rangé, on peut juste écrire la ligne suivante pour n'afficher que "Mathura" :
echo "<b>students[0]['name'] : </b>", $students[0]['name'];
echo "</pre>";

# N.B : On utilise pour désérialiser "json_decode" pour avoir un tableau associatif que l'on pourra donc parcourir comme on veut,
# car chaque élément du tableau a une clé spécifique.
# Avec cette clé, on peut afficher/extraire les informations que l'on souhaite dans l'ordre que l'on souhaite.
# N.B : pour afficher la page sur le navigateur il n'y a rien besoin de faire car on a déjà lancé la commande "php -S localhost:8000".
# Elle lance tous les fichiers php du dossier TP2_PP. Donc on a juste à se rendre à l'adresse http://localhost:8000/exo2.php pour voir le résultat.
?>