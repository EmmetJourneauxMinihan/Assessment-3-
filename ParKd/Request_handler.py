from geopy.geocoders import Nominatim
  
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
  
# entering the location name
getLoc = loc.geocode("34 empire st, footscray")
  
# printing address
print(getLoc.address)
  
# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)
import msvcrt as m
m.getch()