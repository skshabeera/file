f=open("saral1.text","r")
sum=f.readlines()
for z in sum:
    if "delhi " in z:
        a=open("delhi.text","a")
        a.write(z)
        print(a)
    elif "shimla" in z:
        b=open("shimla.text","a")
        b.write(z)
        print(b)
    elif "others" in z:
        c=open("others.text","a")
        c.write(z)
        print(c)
    else:
        pass
f.close()   
        