with open('prosong.txt', 'r') as f:
    p = [line.strip() for line in f]
l=[]
for i in p:
    j=i.replace('-','-->',1)
    l.append(j)
k=[]
s=" id='talonely'"
p=[]
for i in range(len(l)):
    l[i]='&#9654<!--'+l[i]
for i in l:
    i=i.split()
    for j in range(len(i)):
        if(i[j]=='controls'):
            i[j]+=s
    k.append(' '.join(i))
for i in k:
    print(i)
    print()
    
    
    