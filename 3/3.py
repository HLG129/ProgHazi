import sys

def anagramma(args):
    str1=args[1]
    str2=args[2]
    if len(str1)!=len(str2):
        print ('Hamis')
    else:
        for i in str2:
            if i in str1:
                str1=str1.replace(i,'')
        if str1=='':
            print('Igaz')

anagramma(sys.argv)