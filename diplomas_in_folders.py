file = open("input.txt")
array = []
for line in file:
   for numb in line.split():
       array.append(int(numb))
numb_of_folders = array[0]
folders = array[1:]
folders.sort()
folder = 0
sec = 0
while folder != (numb_of_folders - 1):
    sec += folders[folder]
    folder += 1
print(sec)