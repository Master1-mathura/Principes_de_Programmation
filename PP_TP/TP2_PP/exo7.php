<?php
require_once "config/config.php";
require_once "services/StudentService.php";

# Récupération des données via le Service
$students = StudentService::getAllStudents();

# Affichage via la Vue stylisée
require_once "views/students.php";

# N.B : À l'adresse http://localhost:8000/exo7.php on a le même affichage qu'à l'exo6 car ces deux exos partagent le même fichier style.css
?>