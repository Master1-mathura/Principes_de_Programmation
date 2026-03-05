<?php
require_once "config/config.php";
require_once "services/StudentService.php";

# Récupération des données via le Service
$students = StudentService::getAllStudents();

# Affichage via la Vue stylisée
require_once "views/students.php";
?>