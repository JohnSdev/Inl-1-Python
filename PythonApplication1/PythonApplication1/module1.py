
import re
dict = {"name":"Mark", "age":12, "teacher":True}
d=str(dict)
q=d.replace(" ", "")
print(q)
y=[]
g=[]
map={}
for x in dict.keys():
	x.replace("'", '"')
	y.append(x)
	
for f in dict.values():
	g.append(f)

for x in range(len(y)):
	map[x] = g[x]

print(map)

