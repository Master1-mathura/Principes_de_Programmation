import javax.xml.ws.Endpoint;

public class Application {
    public static void main(String[] args) {
        System.out.println("Debut de déploiement de mon service ");
        //on ne va pas utiliser un serveur d'application pour l'instant
        String url = "http://localhost:8888/";//adresse pour publier
        Endpoint.publish(url, new MonserviceWeb());//pour rendre accessible mon service web, deuxieme para = instance du service qu'on veut publier
        System.out.println("Le service web est déployé");
    }
}
//http://localhost:8888/?wsdl pour web service definition language c'est un fichier xml
// localhost:8888/?xsd=1
