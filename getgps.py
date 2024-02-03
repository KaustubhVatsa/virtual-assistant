import geocoder

def currentloc():
    try:
        location = geocoder.ip("me")
        latitude = location.latlng[0]
        longitude = location.latlng[1]
        city =location.city
        country = location.country
        return city
    except Exception as e :
        print(f"failed{e}")

currentloc()
