def pro(u,v):
    a=len(str(u)) #자릿수 계산
    b=len(str(v))
    n=max(a,b)
    if(u==0 or v==0):return 0
    elif(n<=2):return u*v
    else:
        m=n//2
        x=u//(10**m)
        y=u%(10**m)
        w = v // (10 ** m)
        z = v % (10 ** m)
        return pro(x,w)*(10**(2*m))+\
               (pro(x,z)+pro(w,y))*(10**m)+pro(y,z)
def pro2(u,v):
    a=len(str(u)) #자릿수 계산
    b=len(str(v))
    n=max(a,b)
    if(u==0 or v==0):return 0
    elif(n<=2):return u*v
    else:
        m=n//2
        x=u//(10**m)
        y=u%(10**m)
        w = v // (10 ** m)
        z = v % (10 ** m)
        r=pro2(x+y,w+z)
        p=pro2(x,w)
        q=pro2(y,z)
        return p*(10**(2*m))+(r-p-q)*(10**m)+q

print(pro(342,421))
print(pro2(342,421))
print(342*421)