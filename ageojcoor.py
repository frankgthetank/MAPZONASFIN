import geopandas as gpd

# Cargar el archivo .gpkg
gdf = gpd.read_file("ZONADMQ1.gpkg")

# Verifica el sistema de referencia de coordenadas actual
print(f"Sistema de referencia de coordenadas original: {gdf.crs}")

# Si el sistema de coordenadas no es EPSG:4326, lo convertimos a EPSG:4326
if gdf.crs.to_epsg() != 4326:
    gdf = gdf.to_crs(epsg=4326)

# Guardar el archivo en formato GeoJSON con las coordenadas convertidas
gdf.to_file("data_coord.geojson", driver="GeoJSON")

# Verifica el sistema de coordenadas después de la conversión
#print(f"Sistema de referencia de coordenadas después de la conversión: {gdf.crs}")
