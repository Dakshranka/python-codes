def pangram(str):
    a="abcdefghijklmnopqrstuvwxyz"
    for char in a:
        if char not in str.lower():
            return False
            
    return True
    
string=input()
if(pangram(string)== True):
    print("pangram")
else:
    print("not pangram")

