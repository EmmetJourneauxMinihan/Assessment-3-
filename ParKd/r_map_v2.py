import folium
import pandas as pd
import webbrowser as w
import time
import pyautogui
from geopy.geocoders import Nominatim
 

def location_finder(): 
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
     
    dest = input("Please enter where would you like to go:")
    # entering the location name
    getLoc = loc.geocode(dest)
    
    
    # printing address
    print("Taking you to - ", getLoc.address)
    print("Wait.......")
    time.sleep(1)
    
    lat = getLoc.latitude
    long = getLoc.longitude
    
    return lat, long



#Shows a general map
#Geolocation is set for Sydney
#Zooming scale sets at 3
#So australia is visible

def general_map():
    raw_map = folium.Map(
    location = [-33.86223532006098, 151.21162246066174],
    zoom_start = 3
    )
    raw_map.save("map.html")

#Reads the paid.csv file with the pandas module.
#Loads the map.
#Scale the map accroding to the zooming ratio specified.
#Then add the markers using the latitude and longitude retrived from the csv file.


def custom_location(lat, long):
    raw_map = folium.Map(
        location = [lat, long],
        zoom_start = 20
        )
    folium.Marker(
        location =[lat, long]
    ).add_to(raw_map)

    raw_map.save("Custom Location.html")



def free_parking():
    f_parking = pd.read_csv('free_parking.csv')
    free_park = f_parking.loc[5]
    raw_map = folium.Map(
        location = [free_park['latitude'], free_park['longitude']],
        zoom_start = 14.499999999999999
        )
    
    for i in range(len(f_parking)):
        free_park = f_parking.loc[i]
        
        
        
    
        folium.Marker(
            location =[free_park['latitude'], free_park['longitude']]
        ).add_to(raw_map)
    
    raw_map.save("free_park.html")
    

#Reads the paid.csv file with the pandas module.
#Loads the map.
#Scale the map accroding to the zooming ratio specified.
#Then add the markers using the latitude and longitude retrived from the csv file.

def paid_parking():
    p_parking = pd.read_csv('paid_parking.csv')
    paid_park = p_parking.loc[1]
    raw_map = folium.Map(
        location = [paid_park['latitude'], paid_park['longitude']],
        zoom_start = 18
        )
    
    for i in range(len(p_parking)):
        paid_park = p_parking.loc[i]
        
        
        
    
        folium.Marker(
            location =[paid_park['latitude'], paid_park['longitude']]
        ).add_to(raw_map)
    
    raw_map.save("paid_park.html")


#This function is starting point of the application
#Gets choice from the user
#Based on choice, different modules are executed

def show_map():
    
    try:
        choice = input("Choose an option.\n(m)Map\t(f)Free parkings\t(p)Paid parking\t(s)Search")
        if choice == "m":
            general_map()
            w.open_new_tab("map.html")
            
        elif choice == "f":
            free_parking()
            w.open_new_tab("free_park.html")
            pyautogui.moveTo(900, 700)
            time.sleep(.7)
            pyautogui.scroll(1)

        elif choice == "p":
            paid_parking()
            w.open_new_tab("paid_park.html")
            pyautogui.moveTo(900, 770)
            time.sleep(.7)
            pyautogui.scroll(-1)
        
        elif choice == "s":
            (lat, long) = location_finder()
            custom_location(lat, long)
            w.open_new_tab("Custom Location.html")
             
        else:
            raise ValueError
    
    except:
        print("Invalid input. Try again.")
        show_map()



show_map()
# import msvcrt as m
# m.getch()
