n = int(input().strip())
if n%2!=0:
  print("weird")  
elif n%2==0 and n>2 and n<5:
    print("not weird")
elif n%2==0 and n>6 and n<20:
    print("weird")
elif n%2==0 and n>20 and n<100:
    print("not weird") 
