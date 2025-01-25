import sys
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])


indeterminados_nombre(n=5, c="Hola", argumentos=sys.argv)   