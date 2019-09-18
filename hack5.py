no_ofWords=int(input())
a=[]
for _ in range(no_ofWords):
    b=input()
    a.insert(_,b)

d=set(a)
print(len(d))    

for i in range(no_ofWords):
    b=a.count(a[i])
    print(b,end=" ")

    

    
