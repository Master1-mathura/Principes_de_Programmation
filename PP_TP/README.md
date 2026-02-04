# Notes de Cours :

Ce document synthétise les notes de cours (CM1 du 16/01) portant sur les architectures logicielles, les systèmes distribués, la conteneurisation et les protocoles de communication.

## 1. Concepts Fondamentaux du Développement

### Framework vs Bibliothèque (Library)
* **Bibliothèque :** Une boîte à outils où le développeur pioche des fonctions. C'est le développeur qui a le contrôle et appelle le code.
* **Framework (Cadre de travail) :** Structure rigide qui impose une façon de faire.
    * *Objectif :* Automatiser les tâches répétitives et génériques pour se concentrer sur la logique métier.

### Architecture Web
Une application web se divise généralement en deux parties :
1.  **Backend (Serveur) :** Logique métier, accès aux données, souvent dans le Cloud.
2.  **Frontend (Client) :** Interface utilisateur.


## 2. Architectures Logicielles

### Monolithe vs Microservices
* **Monolithe :**
    * Un seul bloc de code déployé.
    * *Problème :* Si une partie tombe en panne, tout peut tomber. Difficile à maintenir et à faire évoluer (passage à l'échelle complexe).
* **Microservices :**
    * Découpage de l'application en petits services indépendants (ex: service de paiement, service d'affichage).
    * *Communication :* Via des messages légers (JSON/XML).
    * *Avantages :*
        * **Scalabilité horizontale :** On peut ajouter des machines pour gérer plus de charge sur un service précis.
        * **Tolérance aux pannes :** Si le service A plante, le service B continue de fonctionner.
        * **Interopérabilité :** Chaque service peut être écrit dans un langage différent.

### Modèle Maître-Esclave (Master-Slave)
* Un nœud **Maître** distribue les tâches.
* Plusieurs nœuds **Esclaves** exécutent le travail.
* *Gestion de panne :* Si un esclave tombe, le maître redistribue. Si le maître tombe, un mécanisme d'élection désigne un nouveau maître.

---

## 3. Déploiement et Conteneurisation (Docker)

L'objectif est de résoudre le problème « ça marche sur ma machine mais pas en prod ».
* **Docker :** Permet de créer des conteneurs standardisés.
* **Conteneur vs Machine Virtuelle (VM) :**
    * Le conteneur partage le noyau (kernel) du système hôte (Linux) -> Plus léger.
    * La VM virtualise tout le matériel (OS complet) -> Plus lourd.
* **Dockerfile :** Fichier texte contenant les instructions pour construire l'image de l'application (le plan de construction).

---

## 4. Middleware et Communication Distribuée

L'objectif est de faire communiquer des objets distants (sur des machines différentes) de manière transparente.

### RMI (Remote Method Invocation)
Technologie propre à **Java**.
* **Principe :** Permet d'invoquer une méthode sur un objet distant comme s'il était local.
* **Fonctionnement :**
    * **Stub (Client) :** Représente l'objet distant côté client. Il sérialise les paramètres.
    * **Skeleton (Serveur) :** Reçoit l'appel, désérialise, exécute la méthode réelle et renvoie le résultat.
    * **Registry :** Annuaire où les objets sont enregistrés pour être trouvés.
* **Limites :** Couplage fort (Java uniquement des deux côtés).

### Evolution des technologies
1.  **RMI :** Java only.
2.  **CORBA :** Multi-langages mais très complexe.
3.  **SOAP / REST :** Standards du Web (les plus utilisés aujourd'hui).

### Comparatif Rapide

| Technologie | Langage | Type | Caractéristique |
| :--- | :--- | :--- | :--- |
| **RMI** | Java | Objet Distant | Facile mais limité à Java |
| **CORBA** | Multilangue | Objet Distant | Complexe à mettre en œuvre |
| **REST / SOAP** | Tous | Web Service | Standard Web, Interopérable |

---

## 5. Services Web : SOAP vs REST

Ce sont des moyens d'implémenter des API pour l'interopérabilité entre applications hétérogènes.

### SOAP (Simple Object Access Protocol)
* **Nature :** Un **Protocole** strict.
* **Format :** Basé exclusivement sur **XML**.
* **Structure :** Utilise une enveloppe (Envelope) pour les messages.
* **Description :** Utilise le **WSDL** (Web Service Description Language) pour décrire les méthodes disponibles (le contrat).

### REST (Representational State Transfer)
* **Nature :** Un **Style d'architecture** (pas un protocole).
* **Format :** Souvent JSON (plus léger), mais peut utiliser XML, TXT, etc.
* **Principe :** Tout est une **Ressource** identifiée par une **URL** (Uniform Resource Locator).
* **Verbes HTTP :** Utilise les méthodes standard du web pour agir sur les ressources :
    * `GET` : Lire / Récupérer
    * `POST` : Créer
    * `PUT` : Modifier / Remplacer
    * `DELETE` : Supprimer

### Cycle de vie d'un appel (RMI/RPC)
1.  Le **Client** appelle la méthode.
2.  Le **Stub** sérialise (transforme en flux de données) les paramètres.
3.  Transfert réseau.
4.  Le **Skeleton** désérialise.
5.  Le **Serveur** exécute le code.
6.  Retour de la réponse (chemin inverse).