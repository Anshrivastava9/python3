#code
test = int(input())

def pattern(num,prev,current):
    if current == num:
        print(num)
        return

    elif prev >0:
        print(current,end= ' ')
        return pattern(num,current-5,current-5)
    else:
        print(current,end= ' ')
        return pattern(num,prev,current+5)


for i in range(test):
    num = int(input())
    print(num,end=" ")
    pattern(num,num,num-5)