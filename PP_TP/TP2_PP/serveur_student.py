from flask import Flask, jsonify, request
#créer l'application flask
app = Flask(__name__)

#une liste d'étudiants
students = [
    {"id" : 1, "name" : "Mathura", "age" : 25},
    {"id" : 2, "name" : "Emna", "age" : 23},
]

#racine de l'API pour tester si le serveur fonctionne
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants !"

# Endpoint pour lister tous les étudiants
@app.route('/students', methods= ['GET'] )
# Méthode HTTP Get qui permet de retourner la liste des étudiants
def get_students():
    """jsonify transforme la liste students en json"""
    return jsonify(students)

# Ajouter un étudiant (POST)
@app.route('/students', methods= ['POST'])
def add_student() :
    new_student=request.get_json()
    # Pour récupérer les données envoyées par le client
    new_student ['id']=len(students)+1
    # Attribuer un numéro (id) de manière incrémentable
    students.append(new_student) # Ajout des données
    return jsonify(new_student), 201
# Le code 201 pour dire création réussie

# Afficher un étudiant sachant son identifiant
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id']==id), None)
    """ autrement dit :
    student = None
    for s in students:
        if s['id'] == id:   #si on trouve l'id
            student = s     #on le sauvegarde
            break
    """
    if student:
        return jsonify(student)
    return jsonify ({"erreur":"l'étudiant n'existe pas !"}), 404

# Mettre à jour un étudiant PUT
@app.route('/students/<int:id>', methods= ['PUT'])
def update_student(id):
    student = next((s for s in students if s['id']==id), None)
    if not student:
        return jsonify ({"message":"Etudiant non trouvé !"}), 404
    data=request.get_json() # Récupération des données envoyées par le client
    student.update(data) # Mise à jour des données
    return jsonify (student)


# Supprimer un étudiant DELETE
"""
# VERSION 1 :
@app.route('/students/<int:id>', methods= ['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['id']!=id]
    return jsonify({"message":"Etudiant supprimé"}),200
    
# VERSION 2 :
"""
@app.route('/students/<int:id>', methods= ['DELETE'])
def delete_student(id):
    student = next((s for s in students if s['id']==id), None)
    if not student:
        return jsonify ({"message":"Etudiant non trouvé !"}), 404
    students.remove(student) # Suppression de l'étudiant
    return jsonify (student)

# Activer mode Debug pour voir les erreurs et recharger automatiquement le serveur, TOUJOURS lancer le serveur en dernier
if __name__ == '__main__':
    app.run(debug=True) #le port n'étant pas précisé, il est par défaut le 5000