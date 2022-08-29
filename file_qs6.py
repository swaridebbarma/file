a=open("question3.txt","r")
k=a.readlines()
for i in k:
    if "delhi" in i:
        z=open("delhi.text","a")
        z.write(i)
        print(z)
    elif "shimla" in i:
        z=open("shimla.text","a")
        z.write(i)
        print(z)
    else:
        z=open("other.text","a")
        z.write(i)
        print(z)
a.close()
    