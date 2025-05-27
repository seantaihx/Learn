'''
Use tuples as keys in a dictionary:
	•	Create a dictionary where the key is a (latitude, longitude) tuple and the value is a city name.
	•	Add three locations.
	•	Print all items in the format:
"City: [name], Coordinates: ([lat], [long])"
'''

locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (37.7749, -122.4194): "San Francisco"
}

for coord, city in locations.items():
    print(f"City: {city}, Coordinates: {coord}")



'''SAMPLE OUTPUT
City: New York, Coordinates: (40.7128, -74.006)
City: Los Angeles, Coordinates: (34.0522, -118.2437)
City: San Francisco, Coordinates: (37.7749, -122.4194)
'''
