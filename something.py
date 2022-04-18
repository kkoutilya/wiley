n,q=map(int,input().split())
dct={}
t=[]
len=0
for i in range(n):
    x,y=map(int,input().split())
    if x in dct:
        dct[x]+=y
        continue
    dct[x]=y
    len+=1
k=dct.keys()
for i in range(q):
    x,y=map(int,input().split())
    c=0
    for a in dct:
        if a>=x and a<=y:
            c+=dct[a]
    t.append(c)
print(*t)