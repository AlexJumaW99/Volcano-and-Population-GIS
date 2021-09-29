import folium
map = folium.Map(location=[48,-120], tiles='Stamen Terrain', zoom_start=4)

import pandas
df = pandas.read_csv('Volcanoes.txt')
#print(df)
elevation = list(df['ELEV'])
lat = list(df['LAT'])
lon = list(df['LON'])
nme = list(df['NAME'])

fg = folium.FeatureGroup(name = 'Volcanoes')
fg2 = folium.FeatureGroup(name = 'Population')

for el,lt,ln,nm in zip(elevation, lat, lon, nme):
    def marker_color(ele):
        if el < 2000:
            col = 'green'   
        elif 2000 <= el < 3000:
            col = 'orange'
        else:
            col = 'red'

        return col
    html = f'''
    Volcano Name: <br>
    <a href = "https://www.google.com/search?q={nm} Volcano" target="_blank">{nm}</a> <br>
    Height : {el}
    '''
    iframe = folium.IFrame(html=html, width=100, height=200)

    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon= folium.Icon(color=marker_color(el))))

fg2.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf=8-sig").read(),
style_function=lambda x:( {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})))
#print(help(folium.IFrame))

map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save('Map2.html')
