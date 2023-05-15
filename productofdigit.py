n=int(input())
def product(n):
    product=1
    for i in str(n):
        product=product*int(i)
    return product
print(product(n))