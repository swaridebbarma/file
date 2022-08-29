my=open("my_file.txt")
m= my.read()
print(m)
my.close()
i=0
c=0
while i<len(m):
    c=c+1
    i+=1
print(c)
