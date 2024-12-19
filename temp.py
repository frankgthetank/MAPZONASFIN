import json

# Abrir el archivo GeoJSON
with open('static/data_coord.geojson', 'r') as f:
    data = json.load(f)

# Imprimir la estructura completa de un solo elemento (por ejemplo, el primer elemento)
elemento = data['features'][0]  # Selecciona el primer elemento en 'features'
print(elemento)

# Imprimir la estructura completa
print(json.dumps(elemento, indent=4))  # Utiliza indent=4 para un formato más legible

