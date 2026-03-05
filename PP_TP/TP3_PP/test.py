from repository import add_student, delete_student, update_student

new_id = None

# création d'un étudiant
try:
    print("Début de tentative d'ajout")
    new_id = add_student("Nouvel_etudiant", 24)
    print(f"Succes, id du nouvel étudiant : {new_id}\n")
except Exception as e:
    print(f"\nL'ajout s'est soldé en un échec :\n{e}")

# Attention, on ne continue que si l'ajout a marché, sinon l'echec de l'ajout => échec du reste => test faux négatif
if new_id :
# modification de l'étudiant nouvellement ajouté
    try:
        print("Début de tentative de modification")
        if update_student(new_id, "Nouvel_etudiant_modifie", 26) :
            print(f"Succes, l'étudiant {new_id} a bien été modifié.\n")
        else :
            print(f"Échec : L'étudiant {new_id} n'a pas été trouvé pour la modification.\n")
    except Exception as e:
        print(f"\nLa modification s'est soldée en un échec :\n{e}")

    # suppression de l'étudiant nouvellement modifié
    try:
        print("Début de tentative de suppression")
        if delete_student(new_id) :
            print(f"Succes, l'étudiant {new_id} a bien été supprimé.\n")
        else :
            print(f"Échec : L'étudiant {new_id} n'a pas été trouvé pour la suppression.\n")
    except Exception as e:
        print(f"\nLa suppression s'est soldée en un échec :\n{e}")

