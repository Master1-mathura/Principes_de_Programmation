<?php
# On cible l'API Flask de port 5000 (comme précisé dans le serveur) :
$url = "http://127.0.0.1:5000/students";

# On récupère le contenu :
$response = file_get_contents($url);

# On affiche le résultat de manière lisible :
echo"<h3>Réponse brute du serveur Python :</h3>";
echo "<pre>";
echo htmlspecialchars($response);
echo "</pre>";

# N.B : On n'a pas désérialisé, on a juste récupéré le corps, le texte brut.
# N.B : pour afficher la page sur le navigateur il faut,
# en parallèle du terminal ouvert sur le serveur lancé par la commande "python3 serveur_student.py",
# ouvrir un terminal sur le exo1.php et lancer la commande "php -S localhost:8000" (et non 5000 car il est réservé au serveur)
# on aura ainsi le résultat affiché à l'adresse http://localhost:8000/exo1.php
?>

