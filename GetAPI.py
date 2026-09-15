import requests

url = "https://10.121.16.118:7010/api/enviar"

response = requests.get(url)

# Verificar si la petición fue exitosa (código 200)
if response.status_code == 200:
    data = response.json()  # Convierte el JSON a un diccionario de Python
    print("Título:", data["title"])
else:
    print("Error:", response.status_code)
