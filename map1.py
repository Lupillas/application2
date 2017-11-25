import folium
map = folium.Map(location=[42.816667, -1.65], zoom_start=15)
fg= folium.FeatureGroup(name="my map")

fg.add_child(folium.Marker(location = [42.816667, -1.65], popup="hi I am a marker", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("map1.html")
