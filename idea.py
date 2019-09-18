
"""l=list(map(int,input().strip().split()))
n=l[0]
m=l[1]
a = list(map(int,input().strip().split()))

b= list((map(int,input().strip().split()))

c= list(map(int,input().strip().split()))
h=0
for i in range(m):
    if b[i] in a:
        h+=1
    if c[i] in a:
        h-=1

print(h)              


a=[1,2,1,3]
print(a.count(1))"""

no_ofWords=int(input())
a=[]
for _ in range(no_ofWords):
    b=input()
    a.insert(_,b)

print(a)    






