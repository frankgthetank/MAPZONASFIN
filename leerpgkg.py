import geopandas as gpd
import fiona 

# Ruta al archivo GeoPackage
ruta_gpkg = r"C:\Users\anali\OneDrive\Documentos\MAPAFINZONAS\DMQ_cruzado.gpkg"

# Listar las capas disponibles en el archivo .gpkg
#capas = gpd.io.file.fiona.listlayers(ruta_gpkg)
print("Capas disponibles en el archivo GeoPackage:")
#or capa in capas:
#    print(f"- {capa}")

# Seleccionar una capa para leer
#capa_seleccionada = capas[0]  # Cambia el índice si deseas leer otra capa
#print(f"\nLeyendo la capa: {capa_seleccionada}")

# Leer la capa seleccionada como un GeoDataFrame
gdf = gpd.read_file(ruta_gpkg)

# Mostrar las primeras filas (head) del GeoDataFrame
print("\nVista previa de los datos:")
print(gdf.head())
