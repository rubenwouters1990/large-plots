import geopandas as gpd
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool
from bokeh.palettes import brewer
from bokeh.plotting import figure
from bokeh.io import export_png, show, output_file

# import shapefile
shapefile = 'path/to/gewestplan.shp'
gdf = gpd.read_file(shapefile)

# convert to geojson
geosource = GeoJSONDataSource(geojson = gdf.to_json())

# create figure
p = figure(title = 'Gewestplan on OpenStreetMap', 
           plot_height = 600 ,
           plot_width = 950, 
           toolbar_location = None)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# add gewestplan layer to figure in transparent red color
p.patches('xs','ys', source = geosource,
          fill_color = 'red',
          fill_alpha = 0.2, 
          line_color = 'red',
          line_width = 0.5)

# add OpenStreetMap layer
p.add_tile(tile_provider='OSM')

# specify output file
output_file("map.html")

# show plot
show(p)
