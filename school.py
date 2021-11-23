file = open("input.txt", "r")
array = []
for line in file:
    for word in line.split():
        array.append(int(word))
print(array)
numb_houses = array[0]
first_house = array[1]
middle = (numb_houses / 2)
print(middle)
while middle > 0:
    first_house = first_house + 1
    middle = middle - 1

print(first_house)
