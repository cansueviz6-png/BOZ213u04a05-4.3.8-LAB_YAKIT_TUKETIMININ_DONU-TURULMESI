# 1 American mile = 1609.344 meteres
# 1 American gallon = 3.785411784 litres

def litres_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons
def miles_gallon_to_liters_100km(miles):
    meters = miles * 1609.344
    gallons = 100 * 1000 / meters
    litres = gallons * 3.785411784
    return litres
print (litres_100km_to_miles_gallon(3.9))
print (litres_100km_to_miles_gallon(7.5))
print (litres_100km_to_miles_gallon(10.))
print (miles_gallon_to_liters_100km(60.3))
print (miles_gallon_to_liters_100km(31.4))
print (miles_gallon_to_liters_100km(23.5))
