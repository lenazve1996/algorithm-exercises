f = open("input.txt")
array = []
for line in f:
    for word in line.split():
        array.append(int(word))
maxint = 0
count = 0
for number in array:
    if number == maxint:
        count += 1
    if number > maxint:
        maxint = number
        count = 1
print(count)
