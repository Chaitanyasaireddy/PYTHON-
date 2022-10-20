strs=[str(i) for i in input().split()]
L=[]
m=[]
t=[]
if(len(strs)<=1):
    L.append(strs)
    print(L)

else:
    for i in strs:
        l=[]
        for j in strs:
            c=0
            for k in i:
                if(k in j):
                    c+=1
            if(c==len(j)):
                l.append(j)
        L.append(l)
        m.append(len(l))
p=set(m)
print(L)
print(m)
for i in p:
    t.append(L[m.index(i)])
print(t)
