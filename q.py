import numpy
n,m=map(int,(input().split()))
a=numpy.array(input().split())
for i in range(n):
    int(a)
print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
print(numpy.std(a,axis=None))
