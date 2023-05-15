import re
s = 'GeeksforGeeks: $#@^&* A computer science portal for geeks'
 
match = re.findall('ek?',s)
print(match)
 
print('Start Index:', match.start())
print('End Index:', match.end())