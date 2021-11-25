file = open("input.txt", "r")
array = []
for line in file:
    for word in line.split():
        array.append(int(word))
numb_houses = array[0]
houses = array[1:]
print(houses[numb_houses / 2])