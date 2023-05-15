def myfunct(num,power):
    if power==0:
        return(1)
    if num==0:
        return(0)
    else:
        return(num**power)
n=int(input())
a=(myfunct(n,3))
print(a)
def getSum(a):
    
    sum = 0
    for digit in str(a): 
      sum += int(digit)      
    print (sum)
getSum(a)


