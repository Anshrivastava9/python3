'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

list1= list(map(int,input().strip().split()))
b=len(list1)
for i in range(len(list1)):
	for j in range(0,b-1):
		if list1[j]>list1[j+1]:
			list1[j],list1[j+1]=list1[j+1],list1[j]
	
	b-=1


print(list1)


#for i in range(len(list1)):
   # for j in range(len())
    
    
