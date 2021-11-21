array = []
result = 0
for i in open('input.txt'):
	array.append(i[:-1])
if array[1] == '0':
	if array[0] == '0' :
		result = array[2]
	elif array[0] != '0' :
		result = '3'
elif array[1] == '1' :
	result = array[2]
elif array[1] == '4' and array[0] != '0' :
	result = '3'
elif array[1] == '4' and array[0] == '0' :
	result = '4'
elif array[1] == '6' :
	result = '0'
elif array[1] == '7' :
	result = '1'
else :
	result = array[1]
res = int(result)
print(res)