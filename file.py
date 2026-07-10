'''f=open("demo.txt")
print(f.read())'''

'''with open("demo.txt")as f:
    print(f.readline())
    print(f.readline())'''

with open("demo.txt","a")as f:
    f.write("appending file to add ")
with open("demo.txt","w")as f:
    f.write(" this is write method" )