def maxofthree(x,y,z):
    if x>z and x>y:
        return x
    elif y>z and y>x:
        return y
    else:
        return z
a=int(input())
b=int(input())
c=int(input())
print(maxofthree(a,b,c))
