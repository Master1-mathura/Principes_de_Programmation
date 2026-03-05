<?php

class StudentService
{
    public static function getAllStudents()
    {
        # On construit l'URL finale en associant la configuration (API_BASE_URL) et la route métier ("/students") :
        $url = API_BASE_URL . "/students";

        # On récupère le contenu :
        $response = file_get_contents($url);

        return json_decode($response, true);
    }
}
?>