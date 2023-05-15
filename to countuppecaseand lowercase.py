s=input()
def test(s):
    uppercase=0
    lowercase=0
    for i in s:
        if i.isupper():
            uppercase=uppercase+1
        if i.islower():
            lowercase=lowercase+1
    print(uppercase)
    print(lowercase)
test(s)