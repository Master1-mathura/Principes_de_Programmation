<?php
//mtn on va faire l'APIRest on va le faire dans service, objet java on va définir une cmasse student service, public static fonction static donc c'est une méthode de classe donc je peux l utiliser sans passer par objet uniquement en tapant le nom de la classe, mtn si je evux def une autre méthode, il faut afire la constante./.... on va séparer les choses puis on va décoder (désrérialise) on extrait le corps de json, apre son a fait un changement dans testAPIrest et donc on doit aussi fair eun changement dans ---- on vca include el, attention syntaxe :: car pas java, 
//design pattern : ne sont accessible que pour ceux qui ont bcp d'expérience, ils ont un controleur (ensemble de méthodes) qui va communiquer avec la v-- et le mo--?
//on va rajouter répertoire : view où on va créer la vue, ce qui est a droite = liste d'étudiants et on va rajouter view, c'est comme factoriser tout le code, il y a uniqueme,t de l'affichege, mtn si je veux chanegr la vue j'ai pas à aller dans l'appel de l'api etc juste à aller dans la view



//php decode --> transofmartion en tableau associatif pour ple parcourir etc
//evolution ----> pour éviter changement partout et sep logique metier etc --> on a
//test en incluant juste config où on va que mettre api_url (on va juste mettre l'url)
//sep service --> classe service student et changer truc en appelant la méthode
//afficaheg pour php et html mtn que vue est là, on va :
//ajouter du style via sous repertoire asset (CSS) ou framework (Boothstrap à fair eau moins une fois à la main et pdt le projet on peut l'use, c'ets un framework CSS avec tempalte déjà fait, soit il est en local soit il est dispo sur le lien)
//