def haromszog(a,b,c):
    if ((a<b+c) and (b<a+c) and (c<a+b)):
        c=True
    else:
        c=False
    return c

while True:
    hsz_old=input('oldalak: ')
    if hsz_old=='end':
        break
    a,b,c = hsz_old.split()
    a=int(a)
    b=int(b)
    c=int(c)
    if haromszog(a, b, c) == True:
        s=(a+b+c)/2
        T=(s*(s-a)*(s-b)*(s-c))**0.5
        print(T)
    else:
        print('A haromszog nem szerkesztheto!')