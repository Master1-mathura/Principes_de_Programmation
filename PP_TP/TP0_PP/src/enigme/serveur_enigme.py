from flask import Flask, jsonify, request
app = Flask(__name__)
app.json.sort_keys = False

#liste des suspects
suspects = [
    {"suspect_num" : 1, "nom" : "Emna", "age" : 23, "lien" : "Sa soeur", "alibi" : "En train de regarder un kdrama (Aucun temoin)"},
    {"suspect_num" : 2, "nom" : "Vidur", "age" : 21, "lien" : "Son ami d'enfance", "alibi" : "Sur le trajet de la fac, en train d'ecouter Spotify (2 temoins)"},
    {"suspect_num" : 3, "nom" : "Omar", "age" : 23, "lien" : "Le delegue de sa classe", "alibi" : "Sur le terrain de volley, blesse a la cheville (12 temoins)"},
    {"suspect_num" : 4, "nom" : "Jacques", "age" : 23, "lien" : "Son voisin", "alibi" : "Dans une superette pour acheter de l'eau (Aucun temoin, pas de camera, a paye en espece)"},
]

@app.route('/')
def home():
    return ("29/01/2026 - Paris Nord City."
            "A l'aube de son anniversaire, Lyes qui faisait son jogging, decouvre le corps sans vie de Mathuro,"
            " poignarde au coeur aux alentours de 23h la veille -larme du crime a ete retrouvee non loin de la"
            " victime dans des buissons. Aussitot avertie, la police a determine la liste des suspects dans cette"
            " affaire sordide et demande l'aide de tous les citoyens de Paris Nord City pour d eventuels temoignages."
            " Pourrez-vous les aider ? ")

@app.route('/suspects', methods= ['GET'] )
def get_suspects():
    return jsonify(suspects)

@app.route('/suspects', methods= ['POST'])
def add_suspect() :
    new_suspect=request.get_json()
    new_suspect ['suspect_num']=len(suspects)+1
    suspects.append(new_suspect)
    return jsonify(new_suspect), 201

@app.route('/suspects/<int:suspect_num>', methods=['GET'])
def get_suspect(suspect_num):
    suspect = next((s for s in suspects if s['suspect_num']==id), None)
    if suspect:
        return jsonify(suspect)
    return jsonify ({"erreur":"Le suspect s'est enfui !"}), 404

@app.route('/suspects/<int:suspect_num>', methods= ['PUT'])
def update_suspect(suspect_num):
    suspect = next((s for s in suspects if s['suspect_num']==id), None)
    if not suspect:
        return jsonify ({"message":"Le suspect s'est enfui !"}), 404
    data=request.get_json()
    suspect.update(data)
    return jsonify (suspect)

@app.route('/suspects/<int:suspect_num>', methods= ['DELETE'])
def delete_suspect(suspect_num):
    suspect = next((s for s in suspects if s['suspect_num']==id), None)
    if not suspect:
        return jsonify ({"message":"Le suspect s'est enfui !"}), 404
    suspects.remove(suspect)
    return jsonify (suspect)

if __name__ == '__main__':
    app.run(debug=True)
