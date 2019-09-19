'''
https://www.hackerrank.com/challenges/words-score/problem

'''





words="ansh shri sandeep shiven"
final=0
b=0
count=0
for i in range(len(words)):
    if words[i]!=" ":
        if words[i] in "aeiou":
            count+=1
        
    else:
        if count==0:
            continue
        else:    
            if count%2==0:
                b=2
            else:
                b=1
            final+=b
        count=0    
           
            
if count==0:
    pass
else:    
    if count%2==0:
        b=2
    else:
        b=1
    final+=b 
            
            
print(final)            
            
    