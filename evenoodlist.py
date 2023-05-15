from tkinter import N


even=[]
odd=[]
for i in range(1,101):
    if i%2==0 :
        even.append(i)
        even.count(i)
    else:
     odd.append(i)
     odd.count(i)
print(even)  
print(odd) 
