import requests
#creation du client pour ajout des students!!
url = "http://127.0.0.1:5000/students"
new_student = {"name": "Personne ajoutée via client_student.py", "age": 23}

# On envoie la requête POST
response = requests.post(url, json=new_student)

print(f"Statut : {response.status_code}")
print(f"Réponse : {response.json()}")