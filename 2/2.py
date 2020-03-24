def atlag(my_file):
    for line in my_file:
        szamok=line.split()
        db=0
        ossz=0
        for szam in szamok:
            if int(szam)>0:
                ossz+=int(szam)
                db+=1
        if db!=0:
            print (ossz/db)
        else:
            print('Nem szamolhato atlag')

try:
    my_file=open('szamok.txt','r')
    atlag(my_file)
except FileNotFoundError:
    print('Hiba')
