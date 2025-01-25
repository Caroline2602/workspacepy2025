def calculadorImcv2(peso,talla):
    tallaMetros=talla/100
    return peso/tallaMetros

def pedirDatosUsuario():
    peso=float(input("Ingrese su peso: "))
    talla=float(input("Ingrese su talla: "))
    imc=calculadorImcv2(peso,talla)
    print(f"el imc de la persona es {imc}")
def calcularLista():
    #codigo de ejercicio5
    pass

pedirDatosUsuario()