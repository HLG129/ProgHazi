import sys

def lista_szetvalaszto(args):
    list1=[]
    list2=[]
    n = int(args[0])
    for arg in args:
        if arg.isdigit():
            continue
        if len(arg)<=n:
            list1.append(arg)
        else:
            list2.append(arg)
    return list1,list2

list1, list2=lista_szetvalaszto(sys.argv[1:])
print(list1)
print(list2)