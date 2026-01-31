// SOAP : simple Object Access Protocol

// annotations utilisées : JAX-WS (XML pour Web Service) basées sur les annotations de JAXB (Java Architecture XML Building) qui permettent la (dé)sérialisation

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService; //annotation obligatoire

@WebService(targetNamespace = "http://...") //seule annotation pour que notre classe soit exposée comme un service web
//espace de nommage -> sert à distinguer de l'exterieur, de quel service on parle
//http://.. si je mets cette adresse sur un navigateur je vais aps accéder à une ressource, donc pour cela, :
/*  URL : Uniform Resource Locator : chaine de caracteres pour accéder aux informations ou à une ressource en utilisant l'adresse de l'emplacement de la ressource
    URN : Uniform Resource Name : ne fournit pas informations sur le protocole pour accéder à la ressource mais fourni des informations sur la ressource elle même (nom ou identification)
    URI : Uniform Resource Identifier : accéder à l'emplacement de la ressource via nom ou addresse ou les deux
    Donc URN + URL = URI
*/
public class MonserviceWeb {

    @WebMethod(operationName = "convertir")
    public double conversion(double mt) {
        return mt * 0.9;
    }

    // l'ajout d'une nouvelle méthode -> pour que le wsdl se réactualise il faut arrêter le service et le redéployer, le wsdl est sauvegardé dans le jmdi (registre de java)
    public double somme(@WebParam(name = "parametre1") double a, double b) {
        return a + b;
    }

//@WebParam(name = "") pour renommer les arguments
//@WebMethod(operationName = "") pour renommer les méthodes

//une fois qu on a créé la classe 2tuditant je veux échanger maintenant des objets sous forme de xml
//via msg SOAP (requete http)

    public Etudiant getEtudiant(int identifiant) {
        return new Etudiant(1, "Mario", 19);
    }
}