<?php
# On cible l'API Flask de port 5000 (comme précisé dans le serveur) :
$url = "http://127.0.0.1:5000/students";

# On récupère le contenu :
$response = file_get_contents($url);

# On désérialise le contenu :
$students = json_decode($response, true);

echo "<h3>Liste des étudiants</h3>";

# On automatise l'affichage :
foreach ($students as $student) {
    echo $student['name'], " - ", $student['age'], " ans<br>";
}
?>