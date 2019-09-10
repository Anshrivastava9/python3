

g=int(input("ENter any Number: "))

y=1
p=g
for b in range(0,g):
    for a in range(0,2):
        for i in range(0,p-1):
            print(" ",end="")
    
        for j in range(0,2*y):
            print("*",end="")
        print("\n")
    p-=1
    
    
    y+=1    