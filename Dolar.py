import requests
import re

# URL de la página de Dolar Hoy
url = "https://dolarhoy.com/cotizaciondolarblue"

# Hacemos la solicitud HTTP a la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Extraemos los valores de cotización como si fuese una peticion CURL
    values = re.findall(r'<div class="value">([^<]+)', response.text)

    # Verificamos si se han encontrado al menos dos valores
    if len(values) >= 2:
        # Asignar los valores a las variables de venta y compra
        venta = values[0].strip().replace('$', '').replace(',', '.')  # Elimina el '$' y cambiar la coma por un punto
        compra = values[1].strip().replace('$', '').replace(',', '.')  # Elimina el '$' y cambiar la coma por un punto

        # Convertimos los valores a float si lo necesitas para operaciones matemáticas
        venta = float(venta)
        compra = float(compra)

        # Mostramos los valores obtenidos
        print(f"Venta: {venta}")
        print(f"Compra: {compra}")
    else:
        print("No se encontraron los valores de cotización.")
else:
    print(f"Error al obtener la página. Código de estado: {response.status_code}")
