import requests

url = "http://10.121.16.118:7010/api/enviar"

payload = {"imagen": [126, 255, 249, 153, 153, 255, 102, 102]}
response = requests.post(url, json=payload)

if response.status_code:  # 201 significa "Creado"
    print("Creado con éxito:")
    print(response.json())
else:
    print("Error:", response.status_code)
