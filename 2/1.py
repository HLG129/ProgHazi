def atlag(x,y):
    atl=(x+y)/2
    return atl

while True:
    try:
        a=input('Adjon meg ket szamot: ')
        x,y=a.split()
        x=int(x)
        y=int(y)
        if ((x>0 and x<100) and (y>0 and y<100)):
            if atlag(x, y) < 60:
                raise Exception('Megbukott!')
            else:
                print (atlag(x,y))
                break
        else:
            raise Exception('Nem megfelelo szam')
    except Exception as e:
        print(e)
