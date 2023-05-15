def divisor(n):
    for i in range(1,n):
        if n%i==0:
            print("{0} is divisible by {1}".format(n, i))
    return(divisor(n))
n=int(input())
print(divisor(n))