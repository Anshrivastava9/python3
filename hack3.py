
        

fptr = open('input01.txt','r')

string=fptr.read().replace('\n','')
k=int(input())
subsegments=len(string)//k

n=0
for i in range(subsegments):
    str1=string[n:k+n]
    str2=list(dict.fromkeys(str1))
    print("".join(str2))
    n+=k