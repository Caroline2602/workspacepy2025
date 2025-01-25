#paso por referencia

#tengo mi variable
# en la funcion se cambia el valor de la variable
# la variable inicial es modificada

lista=[1,2,3,4,5]


def cambiarUltimoElemento(lista:list)->int:
    lista[-1]=lista[0]+100
    return 0

cambiarUltimoElemento(lista)
print(lista)