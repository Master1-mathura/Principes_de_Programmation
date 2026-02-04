Pour ce TP1, nous avons créé un Service Web SOAP (le protocole basé sur XML pour l'échange d'informations) en Java en utilisant les API JAX-WS (Java API for XML Service) et JAXB (Java Architecture for XML Binding).

L'objectif est de mettre en place un service web capable d'effectuer des opérations simples (somme, conversion) et de manipuler des objets complexes (Etudiant) à travers des échanges de messages XML.

Prérequis pour le bon démarrage du TP :
- Java JDK installé.
- Un IDE (IntelliJ IDEA recommandé au vu du fichier .iml). 

Le projet permet de distinguer trois notions fondamentales de l'identifiant de ressource :
- **URL** (Uniform Resource Locator) : Adresse complète permettant d'accéder à la ressource via un protocole (ex: http://...).
- **URN** (Uniform Resource Name) : Identification unique de la ressource par son nom, sans donner d'information sur son emplacement ou son protocole.
- **URI** (Uniform Resource Identifier) : Concept global englobant l'URL et l'URN pour identifier une ressource par son nom, son emplacement, ou les deux.

Le projet est composé des classes suivantes :
- **MonserviceWeb.java** : la classe de service utilise les annotations :
    - @WebService : Indispensable pour exposer la classe comme un service web
    - targetNamespace : Définit l'espace de nommage pour distinguer le service à l'extérieur
    - `@WebMethod`(operationName = "...")' : Permet de renommer l'opération dans le fichier WSDL
    - @WebParam(name = "...") : Permet de personnaliser le nom des arguments dans les messages SOAP

- **Etudiant.java** : Le modèle de données. Pour échanger des objets complexes entre le client et le serveur :
    - **@XmlRootElement** : Annotation JAXB indispensable pour transformer l'objet en XML
    - **Constructeur sans paramètre** : Obligatoire pour le framework, notamment lors de l'utilisation d'injections de dépendances ou de la désérialisation

- **Application.java** : Le déploiement. Le service est publié sans serveur d'application externe (comme GlassFish ou Tomcat) grâce à la classe Endpoint :
    - **URL de publication** : http://localhost:8888/
    - **Instance** : Le service est rendu accessible en passant une instance de MonserviceWeb à la méthode publish.

Pour tester, nous avons lancé la classe Application.java, le message "Le service web est déployé" confirmera la mise en ligne. Une fois le test lancé, nous pouvons vérifier son bon fonctionnement à travers les interfaces :
- **WSDL (Web Service Definition Language)** : Document XML décrivant les méthodes disponibles, accessible via http://localhost:8888/?wsdl.
- **XSD (XML Schema Definition)** : Définit la structure des données (ex: l'objet Etudiant), accessible via http://localhost:8888/?xsd=1.

Le WSDL est sauvegardé dans le registre Java (JMDI). Si vous ajoutez une méthode ou modifiez une signature, vous devez arrêter et redéployer le service pour que le WSDL se réactualise.

Le service propose trois opérations principales :
- **convertir** : Convertit un montant (par exemple, multiplication par 0.9)
- **somme** : Calcule la somme de deux nombres. L'un des paramètres est explicitement nommé parametre1.
- **getEtudiant** : Retourne une instance d'un objet Etudiant sérialisée en XML.

