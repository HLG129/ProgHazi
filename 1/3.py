def mgh_szam(szo):
    db=0
    mgh='aeiou'
    szo.lower()
    for i in szo:
        if i in mgh:
            db+=1
    return db

szo=input('Szo: ')
print(mgh_szam(szo))