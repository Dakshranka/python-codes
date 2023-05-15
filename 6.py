a=input()
b=[]
for i in a:
    b.append(i)
if b[1]==b[2] or b[0]==b[1] or b[0]==b[2]:
    print("bad")
else:
    print("good")