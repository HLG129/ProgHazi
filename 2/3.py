import string
def szavak(my_file):
    out_file=open('Hazi.txt','w')
    for line in my_file:
        new_str=''
        for ch in line:
            if ch not in string.punctuation:
                new_str+=ch
        tmp=new_str.split()
        for szo in tmp:
            if len(szo)>1:
                if (szo[0].lower()==szo[len(szo)-1].lower()):
                    print(szo,file=out_file)

    out_file.close()
try:
    my_file=open('szoveg.txt','r')
    szavak(my_file)
    my_file.close()
except FileNotFoundError:
    print('Hiba')
