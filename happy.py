def sum_sqr(num):
    x=0
    for i in range(len(str(num))):
        y= str(num)
        x= x+ int(y[i])*int(y[i])
        print(x)
    if len(str(x)) !=1:
       return sum_sqr(x)
    elif x ==1:
        return True
    else:
        return False
n = int(input('enter the desired number:'))
print(sum_sqr(n))