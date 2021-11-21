with open("input.txt", "r") as f:
	text = f.readline()
array = text.split()
number_of_stations = int(array[0])
start = int(array[1])
finish = int(array[2])
result = finish - start
if result < 0:
	result = result * -1
if result > number_of_stations / 2:
	if start > finish:
		tmp = start
		start = finish
		finish = tmp
	result = number_of_stations - finish + start
print(result - 1)