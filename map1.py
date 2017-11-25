import folium
import pandas

data = pandas.read_csv("volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
names= list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[46.1997986,-122.1809998], zoom_start=6)
fg= folium.FeatureGroup(name="my map")


for lt, ln, el, nm in zip(lat,lon, elev, names):
    pup=folium.Popup("Nombre: "+nm,parse_html=True)
    fg.add_child(folium.CircleMarker(location = [lt,ln], radius=6, popup=pup, fill=True, fill_color=color_producer(el),color = 'grey',fill_opacity=0.3))

map.add_child(fg)
map.save("map1.html")
