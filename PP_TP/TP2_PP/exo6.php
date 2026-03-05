<?php
# On charge la configuration (l'URL de base)
require_once "config/config.php";

# On charge le Service
require_once "services/StudentService.php";

# Le contrôleur (exo6.php) récupère les données :
$students = StudentService::getAllStudents();

# Le contrôleur passe le relais à la Vue pour l'affichage :
require_once "views/students.php";


# N.B : À l'adresse http://localhost:8000/exo6.php on a un affichage nettement plus stylisé et propre, avec une animation.
?>

