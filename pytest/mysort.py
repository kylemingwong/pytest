


a=[[133,135,105],[11,118,52],[85,116,214]]
newlist=[]
for item in a:
    for i in item:
        newlist.append(i)
print newlist




newlist2=[]
for item in a:
    newlist2 = newlist2 + item
print newlist



from compiler.ast import flatten

a = [[34,67,[112,[45]]],34,[1,2,[34,9]]]

b = flatten(a)

print b