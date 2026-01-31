import requests

url = "http://127.0.0.1:5000/suspects"
new_suspect = {"suspect_num" : 5, "nom" : "Ilyes", "age" : 23, "lien" : "Son cousin", "alibi" : "En train de nouer ses lacets (Aucun temoin)"}

response = requests.post(url, json=new_suspect)

print(f"Statut : {response.status_code}")
print(f"Réponse : {response.json()}")