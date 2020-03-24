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
    else:
        a,b,c=hsz_old.split()
        print (haromszog(int(a),int(b),int(c)))