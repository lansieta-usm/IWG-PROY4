import requests
import base64

url = 'https://api.carbonkit.net/3.6/categories/Great_Circle_flight_methodology/calculation?type=great+circle+route&values.IATAcode1=LHR&values.IATAcode2=LAX'
username = 'gabo'
password = 'gabo2505'

credentials = f"{username}:{password}"
credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
headers = {'Authorization': f'Basic {credentials_encoded}'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    xml_content = response.content
    print("nice")
    # Resto del código para procesar el XML
else:
    print(f'Error en la solicitud HTTP: {response.status_code}')