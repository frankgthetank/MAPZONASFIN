from flask import Flask, render_template, request, jsonify
import json
import requests
import base64
import os

# Variables
repo_owner = 'frankgthetank'
repo_name = 'MAPZONASFIN'
file_path = 'static/data_coord.geojson'
branch = 'main'  # o 'master' según sea necesario

# Cargar la clave de la API de Google desde las variables de entorno
google_api_key = os.getenv('GOOGLE_API_KEY')
if not google_api_key:
    print("Error: GOOGLE_API_KEY no está configurado en las variables de entorno.")
    exit()

# Cargar el token de GitHub desde las variables de entorno
token = os.getenv('GITHUB_TOKEN')
if not token:
    print("Error: GITHUB_TOKEN no está configurado en las variables de entorno.")
    exit()

# Inicializar la aplicación Flask
app = Flask(__name__)

@app.route('/config')
def config():
    return jsonify({'googleApiKey': google_api_key})

# Ruta para la página principal (la raíz del servidor)
@app.route('/')
def index():
    return render_template('index.html')  # Aquí renderizas tu archivo HTML con Mapbox

# Ruta para recibir los IDs seleccionados desde el frontend
@app.route('/guardar-ids', methods=['POST'])
def guardar_ids():
    data = request.get_json()
    selected_ids = data.get('selectedIds', [])
    selected_category = data.get('categoria', None)  # Obtener la categoría seleccionada

    # URL del archivo en el repositorio de GitHub
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'

    # Realizar la solicitud GET para obtener el contenido del archivo desde GitHub
    response = requests.get(url, headers={'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github.v3+json'})
    
    if response.status_code == 200:
        geojson_data = response.json()  # Cargar datos del archivo geojson de GitHub

        # Filtrar las features que tienen un ID "zon" en selected_ids
        features_to_update = [feature for feature in geojson_data['features'] if feature['properties']['zon'] in selected_ids]

        # Realizar las modificaciones (por ejemplo, actualizar la categoría)
        for feature in features_to_update:
            feature['properties']['categoria'] = selected_category  # Cambiar la categoría

        # Convertir los datos actualizados en un JSON
        new_content = json.dumps(geojson_data)

        # Obtener el SHA actual del archivo
        file_info = response.json()
        sha = file_info['sha']

        # Preparar el nuevo contenido codificado en base64
        new_content_encoded = base64.b64encode(new_content.encode()).decode()

        # Crear el payload para actualizar el archivo
        data_update = {
            'message': 'Actualizando el archivo GeoJSON',
            'content': new_content_encoded,
            'sha': sha,
            'branch': branch
        }

        # Enviar la solicitud PUT para actualizar el archivo
        update_response = requests.put(url, headers={'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github.v3+json'}, json=data_update)

        if update_response.status_code == 200:
            return jsonify({"message": "Archivo actualizado exitosamente!"})
        else:
            return jsonify({"error": f"Error al actualizar el archivo en GitHub. Código: {update_response.status_code}"}), 400
    else:
        return jsonify({"error": f"Error al obtener el archivo de GitHub. Código: {response.status_code}"}), 400


if __name__ == '__main__':
    # Asegurarse de que Flask use el puerto adecuado en Render (o en cualquier entorno de producción)
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))


