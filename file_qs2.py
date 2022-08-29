my_file=open("people1-exercise.txt")
my_data = my_file.read()
print(my_data)
my_file.close()
i=0
c=0
while i<len(my_data):
    if my_data[i]=="\n":
        c=c+1
    i+=1
print("number of lines Count:",c)