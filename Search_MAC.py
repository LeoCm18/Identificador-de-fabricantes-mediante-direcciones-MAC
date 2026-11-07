import requests

mac_address = input("Escribe tu dirección MAC: ").strip()

url = f"https://api.macvendors.com/{mac_address}"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        print(f"Vendor: {response.text}")

    elif response.status_code == 404:
        print("Fabricante no encontrado")

    elif response.status_code == 429:
        print("Demasiadas solicitudes")

    else:
        print(f"Error HTTP: {response.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Error de conexión: {error}")