file = open("input.txt", "r")
array = []
for line in file:
    for word in line.split():
        array.append(int(word))
if array[0] == array[1] and array[0] <= 12:
    print(1)
elif (array[0] > 12 or array[1] > 12):
    print(1)
else:
    print(0)