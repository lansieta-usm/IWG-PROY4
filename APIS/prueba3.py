import requests
import json

def generate_qr_code(access_token, qr_code_text, frame_name, image_format, qr_code_logo):
    url = f"https://api.qr-code-generator.com/v1/create?access-token={access_token}"
    payload = {
        "frame_name": frame_name,
        "qr_code_text": qr_code_text,
        "image_format": image_format,
        "qr_code_logo": qr_code_logo
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("viva chile")
        content = response.content

        #qr_code_data = response.json()
        #qr_code_url = qr_code_data["url"]
        return None#qr_code_url
    else:
        print(f"Error al generar el código QR. Código de estado: {response.status_code}")
        return None

if __name__ == "__main__":
    access_token = "KjmHYEVfgzYRteWqDGPh5Wa15VXBPfKUdmnzX9AwJIjCYNVjHMTTvEhLO2WMpB9m"  
    qr_code_text = "https://www.google.com/?hl=es"
    frame_name = "no-frame"
    image_format = "SVG"
    qr_code_logo = "scan-me-square"

    qr_code_url = generate_qr_code(access_token, qr_code_text, frame_name, image_format, qr_code_logo)
    if qr_code_url:
        print(f"Código QR generado: {qr_code_url}")
