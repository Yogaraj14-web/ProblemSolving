p=int(input())
c=0
i=1
while i*i <= p:
    if p%i==0:
        c+=1
        if p/i!=i:
            c+=1
    i+=1
if c==2:
    print("Prime")  
else:
    print("not Prime")              