<?php
# On charge la configuration (l'URL de base)
require_once "config/config.php";

# On charge le Service
require_once "services/StudentService.php";

# On appelle le service
$students = StudentService::getAllStudents();

echo "<h3>Liste des étudiants</h3>";

# On automatise l'affichage :
foreach ($students as $student) {
    echo $student['name'], " - ", $student['age'], " ans<br>";
}

# N.B : À l'adresse http://localhost:8000/exo5.php on a le même affichage que l'exo4 mais on a séparé la logique métier (Service) de l'affichage.
?>