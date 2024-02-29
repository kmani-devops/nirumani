a = int (input("A = "))
b = int (input("B = "))
operation = input ("Add/Sub/Mul/Div = ")

if (operation=="Add"):
    c = a+b
    print ("Add =", c)
elif (operation=="Sub"):
    d=a-b
    print ("Sub =", d)
elif (operation=="Mul"):
    e=a*b
    print ("Mul =", e)
elif (operation=="Div"):
    f=a/b
    print ("Div =", f)
else:
    print ("Invalid Operation.")
