#Write your totalPrime function here.
def totalPrime(S,E):
    count=0
    primelist=[]
    for n in range(S,E+1):
        for i in range(2,n+1):
            if n%i == 0:
                count=count+1
        if count<=1:
            primelist.append(n)
        else:
            pass
        count=0
    l=len(primelist)
    return l

#Taking S and E space seperated input.
S,E = map(int,input().split(' '))
print(totalPrime(S,E))


