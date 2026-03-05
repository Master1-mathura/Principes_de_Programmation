from db import get_connection

# LECTURE, trouver tous les étudiants :
def get_all_students():
    
    # appel de dp pour ouvrir le canal de communication via les identifiants
    conn = get_connection()
    # cursor = objet qui va réellement exécuter les commandes SQL sous forme de dictionnaire
    cursor = conn.cursor(dictionary=True)
    
    # envoi la commande SQL brute au serveur :
    cursor.execute("SELECT * FROM students")
    # vide le curseur et transfère tous les résultas de la requête dans la variable result :
    result = cursor.fetchall()
    
    # libération de la mémoire et fermeture de la ligne :
    cursor.close()
    conn.close()
    
    return result

# LECTURE, trouver un étudiant par son identifiant :
def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id))
    result = cursor.fetchone() # l'identifiant étant unique, on ne récupère qu'un seul résultat
    cursor.close()
    conn.close()
    return result

# CRÉATION, ajouter un étudiant :
def add_student(name, age):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO students (name, age) VALUES (%s,%s)" # sql ="..." -> ajout d'une ligne dans la table ; %s -> ici sont des emplacelements réservés
    cursor.execute(sql, (name, age)) 
    conn.commit() # pour enregistrer la ligné ajoutée
    new_id = cursor.lastrowid # attribution d'id à l'étudiant nouvellement ajouté
    cursor.close()
    conn.close()
    return new_id

# SUPPRESSION, effacer un étudiant :
def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    # Attention, pas : WHERE id = %s", student_id) --> car execute attent un itérable (tuple/liste)
    conn.commit()
    rows_affected = cursor.rowcount # pour vérifier si une ligne a été supprimée
    cursor.close()
    conn.close()
    return rows_affected > 0 # une ligne a au moins dû être supprimée

# MODIFICATION, mise à jour d'un étudiant :
def update_student(student_id, name, age):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE students SET name = %s, age = %s WHERE id = %s"
    cursor.execute(sql,(name, age, student_id))
    conn.commit()
    # pour savoir si SQL a trouvé une ligne sur laquelle appliquer la requête et donc si une ligne a bien été modifiée :
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0