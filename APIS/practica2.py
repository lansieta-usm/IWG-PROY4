# con json

import requests
import json

if __name__ == "__main__":
    url = "https://httpbin.org/get"
    args = {"nombre": "Gabriel", "curso": "aprender a usar apis"}
    response = requests.get(url, params=args)
    #print(response.url)
    if response.status_code == 200:
        """
        response_json = response.json() #dic
        origin = response_json["origin"]
        print(origin)
        """
        response_json= json.loads(response.text)
        origin = response_json["origin"]
        print(origin)
