cities = (
    ("New York", 40.7128, -74.0060),
    ("Tokyo", 35.6895, 139.6917),
    ("InvalidCity", 120.0000, -250.0000),
    ("Sydney", -33.8688, 151.2093),
    ("Paris", 48.8566, 2.3522),
    ("Tokyo", 35.6895, 139.6917)
)

for i in range(len(cities)):

    if (cities[i][1] < -90 or cities[i][1] > 90) and (cities[i][2] < -180 or cities[i][2] > 180):
        print("Both the latitude and longitude of the coordinates of {} is invalid".format(cities[i][0]))
    elif cities[i][1] < -90 or cities[i][1] > 90:
        print("The latitude of {} is invalid".format(cities[i][0]))
    elif cities[i][2] < -180 or cities[i][2] > 180:
        print("The longitude of {} is invalid".format(cities[i][0]))
    else:
        continue

for i in range(len(cities)):

    num = cities.count(cities[i])
    if num != 1:
        if i != cities.index(cities[i]):
            continue
        print("{} is entered {} times".format(cities[i][0], num))


'''If want to check the city name rather than the whole tuples

city_names = [c[0] for c in cities]  # 提取城市名
for name in set(city_names):  # 去重
    count = city_names.count(name)
    if count != 1:
        print("{} is entered {} times".format(name, count))
'''

'''Explanation
we have an immutable tuple
i check if the cities's latitude or longitude or both is valid or not
    latitude is -90 < x < 90 and longitude is -180 < y < 180
if it's invalid, print it out

then, i loop through the cities to see if there's any duplicated cities and print it out
if i != cities.index(cities[i]) means if i is not appearing the first time
    index() returns the first index the value occurs
then continue means ignore it, so the print only prints the first occurrence of the duplicated city
'''

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/8Collections (main) $ python 8.3Tuple_Practice.py

Both the latitude and longitude of the coordinates of InvalidCity is invalid
Tokyo is entered 2 times

@seantaihx ➜ .../Practice/Python/Guide/8Co
'''