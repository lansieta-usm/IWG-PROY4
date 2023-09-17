from urllib.parse import quote

def url_to_qr(text):
    # Codificar el texto en URL
    
    encoded_text = quote(text)
    
    # Crear la URL con el texto codificado
    url = f"https://api.qrserver.com/v1/create-qr-code/?data={encoded_text}"
    
    return url
