import re
pan=input()
if len(pan)==10:
    re.findall("\w",pan[0:6])
    re.findall("\d",pan[6:10])
    re.findall("\w",pan[10:])
    print("valid: ",pan)
else:
    print("invalid")