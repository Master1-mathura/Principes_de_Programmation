<?php
/*
 * FICHIER DE CONFIGURATION
 * On isole ici uniquement l'adresse de base du serveur (le "domaine" ou l'IP) -> http://127.0.0.1:5000.
 * Car si le serveur déménage (ex: passage en ligne), on ne modifie que ce fichier.
 * N.B : On ne stocke pas les routes (comme "/students") ni les paramètres ici.
 * Car ces éléments définissent le "contrat d'API" (l'interface). S'ils changent, 
 * c'est le code de l'application lui-même qu'il faudra modifier, pas la configuration.
 */

define('API_BASE_URL', 'http://127.0.0.1:5000');