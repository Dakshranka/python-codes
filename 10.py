n=int(input())
mem=int(input())
team=[]
members=[]
for i in range(n):
    team.append(input())
for i in range(n):
    members_name=[]
    for i in range(mem):
        members_name.append(input())
    members.append(members_name)
print(set(team))
print(members)
dic={}
for i in range(n):
    dic.update({team[i]:members[i]})
print(dic)
name=input()
for i in dic.values():
    if (i.count(name)==1):
        s=members.index(i)
        break
print(team[s])