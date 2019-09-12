s=input()
v=len(s)
for j in s:
    if j in"AEIOU":
        for i in range(s.index(j),v+1):
            print(s[s.index(j):i])
            


    	#if j not in "AEIOU":	



