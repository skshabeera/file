f=open("siri.txt","r")
sum=f.readlines()
for z in sum:
    if "python" in z:
        a=open("python.txt","a")
        a.write(z)
        print(a)
    elif "java" in z:
        b=open("java.txt","a")
        b.write(z)
        print(b)
    elif "js" in z:
        c=open("js.txt","a")
        c.write(z)
        print(c)
    else:
        pass