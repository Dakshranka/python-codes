def table(n,i):
    if i>10:
        return
    print(n,"*",i,"=",n*i)
    return table(n,i+1)
num=int(input())
a=table(num,1)
print(a)

