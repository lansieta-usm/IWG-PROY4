import requests
import json

def generate_qr_code(qr_code_text):#funcion que convierte la url en qr
    access_token = "KjmHYEVfgzYRteWqDGPh5Wa15VXBPfKUdmnzX9AwJIjCYNVjHMTTvEhLO2WMpB9m"  #clave para usar api
    frame_name = "no-frame" #lineas por defecto para usar la api
    image_format = "SVG"
    qr_code_logo = "scan-me-square"

    url = f"https://api.qr-code-generator.com/v1/create?access-token={access_token}" #url de la api
    payload = { #parametros para usar la api
        "frame_name": frame_name,
        "qr_code_text": qr_code_text,
        "image_format": image_format,
        "qr_code_logo": qr_code_logo
    }

    response = requests.post(url, json=payload)#obtiene la info de la api

    if response.status_code == 200:#si la api funciona
        content = response.content #guarda el qr en una variable
        return content
    else:
        print(f"Error al generar el código QR. Código de estado: {response.status_code}")#si marca error, se ve el error
        return None
 
qr_code_text = "ejemplo"
qr_code_url = generate_qr_code(qr_code_text)
#print(qr_code_url)#qr en formato svg, el html lo convierte a una imagen