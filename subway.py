with open("input.txt", "r") as f:
	text = f.readline() 
array = text.split()
number_of_stations = int(array[0])
start = int(array[1])
finish = int(array[2])
try1 = abs(start - finish) - 1
try2 = number_of_stations - try1 - 2
print(min(try1, try2))