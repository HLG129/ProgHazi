import sys, random

def szetvalaszto(args):
    list1=[]
    list2=[]
    eredmeny=[]
    n=int(args[0])
    file_name=args[1]
    out_file=open(file_name,"w")
    for i in range(n):
        num=int(random.randint(0,10))
        list1.append(num)
    print('Elso lista: ', *list1, sep=' ', file=out_file)
    for i in range(n):
        num=int(random.randint(0,10))
        list2.append(num)
    print('Masodik lista: ', *list2, sep=' ', file=out_file)
    for i in range(n):
        j=n-i-1
        eredmeny.append(list1[i]*list2[j])
    print('Eredmeny: ', *eredmeny, sep=' ', file=out_file)

    out_file.close()

szetvalaszto(sys.argv[1:])