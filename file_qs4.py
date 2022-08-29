f=open("file-question4.txt","w")
a = ["Kotak","HDFC","RBL","SBI","Bank of Baroda"]
i=0
while i<len(a):
    f.write(a[i])
    f.write("\n")
    i+=1
print(f)