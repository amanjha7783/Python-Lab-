import ee
ee.Initialize()

# Load Landsat 8 Collection 2 LST
landsat = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2") \
    .filterDate("2023-04-01", "2023-06-30") \
    .filterBounds(delhi_geometry) \
    .filter(ee.Filter.lt("CLOUD_COVER", 10)) \
    .mean()

# LST conversion
lst = landsat.select("ST_B10").multiply(0.00341802).add(149.0).subtract(273.15)