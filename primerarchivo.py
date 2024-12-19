import geopandas as gpd

# Ruta al archivo de entrada
input_gpkg = r"C:/Users/anali/OneDrive/Documentos/PYTHON/1701_DISTRITO_METROPOLITANO_DE_QUITO/1701_DISTRITO_METROPOLITANO_DE_QUITO.gpkg"

# Nombre de la capa que quieres extraer
layer_name = "zon_a"

# Lista de columnas que deseas conservar
columns_to_keep = ["zon","geometry"]  # Reemplaza con los nombres reales

# Ruta al archivo de salida
output_gpkg = "C:/Users/anali/OneDrive/Documentos/PYTHON/1701_DISTRITO_METROPOLITANO_DE_QUITO/ZONADMQ1.gpkg"

# Leer la capa específica del archivo .gpkg
gdf = gpd.read_file(input_gpkg, layer=layer_name)

# Filtrar las columnas que deseas conservar
filtered_gdf = gdf[columns_to_keep]

# Crear una nueva columna llamada 'categoria' con el valor "A"
filtered_gdf["categoria"] = "C"

# Guardar el resultado en un nuevo archivo .gpkg
filtered_gdf.to_file(output_gpkg, layer=layer_name, driver="GPKG")

print(f"El archivo filtrado se guardó en {output_gpkg}")