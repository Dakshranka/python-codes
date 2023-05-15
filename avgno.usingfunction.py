n=int(input())
def average():
    sum=0
    for i in range(n):
        sum=sum+int(input())
    return(sum/n)
a=average()
print(format(a,'.2f'))


   
    
    