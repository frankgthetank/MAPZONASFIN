import json

def leer_elemento_por_id(ruta_archivo, id_buscar):
    # Cargar el archivo GeoJSON
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        geojson_data = json.load(archivo)
    
    # Buscar el elemento con el ID dado
    for feature in geojson_data['features']:
        if feature['properties'].get('zon') == id_buscar:  # Cambia 'man' si el identificador tiene otro nombre
            return feature
    
    # Si no se encuentra, retornar un mensaje o None
    return None

# Ruta del archivo GeoJSON
ruta_geojson = r"C:\Users\anali\OneDrive\Documentos\MAPAFINZONAS\static\data_coord.geojson"

# ID que deseas buscar
id_deseado = "170150189"

# Leer el elemento
elemento = leer_elemento_por_id(ruta_geojson, id_deseado)

# Mostrar el resultado
if elemento:
    print("Elemento encontrado:")
    print(json.dumps(elemento, indent=2, ensure_ascii=False))
else:
    print(f"No se encontró un elemento con el ID {id_deseado}.")
