n=int(input())
s=[False]*(n+1)
for i in range(2,n+1):
    s[i]=True
print(s)
i=2
while i<=n:
    if s[i]==True:
        j=i*i
        while j<=n:
            s[j]=False
            j+=i
    print(s)    
    i+=1
print([x for x in range(2, n + 1) if s[x]==True])
  
         


