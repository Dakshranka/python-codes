n=int(input())
a=[]
for i in range(n):
    b=[]
    name=input()
    model=input()
    b.append(name)
    b.append(model)
for i in range(n):
    year=input()
    price=input()
    b.append(year)
a.append(b)
c=[]
c.append(price)
if price.isdigit==True:
    c.sort(reverse=True)
a.append(c)
print(a)
