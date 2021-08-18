import folium
import pandas as pd

raw_map = folium.Map(
    location = [-33.89242, 151.203756],
    zoom_start = 2
)
raw_map

f_parking = pd.read_csv('free_parking.csv')
f_parking.head(4)

free_park = f_parking.loc[0]
folium.Marker(
    location =[free_park['latitude'], free_park['longitude']]
).add_to(raw_map)

raw_map
