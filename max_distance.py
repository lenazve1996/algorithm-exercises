file = open("input.txt")
array = []
array = file.readline().split()
houses = []
shops = []
i = 0
for c, value in enumerate(array):
    if value == '1':
        houses.append(c)
    elif value == '2':
        shops.append(c)
max_distance = 0
for house in houses:
    nearest_shop = 9
    for shop in shops:
        current_distance = abs(house - shop) 
        if current_distance < nearest_shop:
            nearest_shop = current_distance
    if nearest_shop > max_distance:
        max_distance = nearest_shop
print(max_distance)