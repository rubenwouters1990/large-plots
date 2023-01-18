import geopandas as gpd
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool
from bokeh.palettes import brewer
from bokeh.plotting import figure
from bokeh.io import export_png, show, output_file

# import shapefile
shapefile = 'path/to/gewestplan.shp'
gdf = gpd.read_file(shapefile)

# filter out polygons smaller than 2500 square meters
gdf = gdf[gdf.geometry.area > 2500]

# convert to geojson
geosource = GeoJSONDataSource(geojson = gdf.to_json())

# define color palettes
palette = brewer['YlGn'][8]
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 100)

# create figure
p = figure(title = 'Gewestplan on OpenStreetMap', 
           plot_height = 600 ,
           plot_width = 950, 
           toolbar_location = None)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# add polygons to figure
p.patches('xs','ys', source = geosource,
          fill_color = {'field' :'area', 'transform' : color_mapper},
          line_color = 'black', 
          line_width = 0.25, 
          fill_alpha = 1)

# add colorbar
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
                     border_line_color=None,location = (0,0), orientation = 'horizontal')
p.add_layout(color_bar, 'below')

# add gewestplan layer to figure in transparent red color
p.patches('xs','ys', source = geosource,
          fill_color = 'red',
          fill_alpha = 0.2, 
          line_color = 'red',
          line_width = 0.5)

# add OpenStreetMap layer
p.add_tile(tile_provider='OSM')

# add hover tool
hover = HoverTool(tooltips=[('Area', '@area{0.00} m^2')])
p.add_tools(hover)

# specify output file
output_file("map.html")

# show plot
show(p)
