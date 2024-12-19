import json
import pyproj

# Cargar el archivo .geojson
with open('static/data.geojson', 'r') as f:
    geojson_data = json.load(f)

# Crear el objeto Proj para UTM y WGS84
utm_proj = pyproj.Proj(init="epsg:32717")  # Cambia esto si sabes que es otro UTM
latlng_proj = pyproj.Proj(init="epsg:4326")

# Función para convertir las coordenadas UTM a lat/lng
def convert_utm_to_latlng(utm_coords):
    lon, lat = pyproj.transform(utm_proj, latlng_proj, utm_coords[0], utm_coords[1])
    return [lon, lat]

# Verificar y convertir las coordenadas
for feature in geojson_data['features']:
    if feature['geometry']['type'] == 'MultiPolygon':
        for polygon in feature['geometry']['coordinates']:
            for i, coord in enumerate(polygon[0]):
                print("Coordenada original (UTM):", coord)
                converted_coord = convert_utm_to_latlng(coord)
                print("Coordenada convertida (Lat/Lng):", converted_coord)
