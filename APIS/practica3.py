import requests
import json

if __name__ == "__main__":
    url = "https://httpbin.org/post"
    payload = {"nombre": "Gabriel", "curso": "aprender a usar apis"}

    response = requests.post(url, json=payload)
    #print(response.url)
    #json post se encarga de serializar el archivo json 
    
    if response.status_code == 200:
        print(response.content)
