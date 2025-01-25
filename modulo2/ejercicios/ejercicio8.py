import sys
print(sys.argv)

def indeterminados_posicion(*args):
    for i,arg in enumerate(args):
        print(i,"=>",arg)
indeterminados_posicion(*sys.argv)