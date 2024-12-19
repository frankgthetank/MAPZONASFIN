import geopandas as gpd

# Leer el archivo .gpkg con GeoPandas
gpkg_file = 'data.gpkg'
gdf = gpd.read_file(gpkg_file)

# Guardar el GeoDataFrame como un archivo .geojson
geojson_file = 'data_file.geojson'
gdf.to_file(geojson_file, driver='GeoJSON')

print(f"Archivo convertido a GeoJSON: {geojson_file}")