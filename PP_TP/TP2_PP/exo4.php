<?php
# On charge le fichier de configuration centralisé qui contient l'URL de base (le domaine) :
require_once "config/config.php";

# On construit l'URL finale en associant la configuration (API_BASE_URL) et la route métier ("/students") :
$url = API_BASE_URL . "/students";

# On récupère le contenu :
$response = file_get_contents($url);

# On désérialise le contenu :
$students = json_decode($response, true);

echo "<h3>Liste des étudiants</h3>";

# On automatise l'affichage :
foreach ($students as $student) {
    echo $student['name'], " - ", $student['age'], " ans<br>";
}

# N.B : À l'adresse http://localhost:8000/exo4.php on a le même affichage que l'exo3 avec un code "plus propre" :
# la configuration (l'URL de l'API) est centralisée.
?>