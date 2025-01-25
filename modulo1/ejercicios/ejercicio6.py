# hacer un programa para el personal del banco que calcule la cantidad a aprobar un credito
# parametros , preguntar sobre salario , d/i, propiedades , riesgo financiero , tarjetas credito
# reglas de negocio
#  1. maximo prestamo es en 36 cuotas
#  2. maximo de cuota es 50% ( si no presenta deudas , riesgo financiero < 0.3 y que tenga 
#  alguna propiedad con un valuacion minima al doble de lo prestado)
#  3. maximo de cuota de 20% si tiene el riesgo financiero de 0.5 maximo
#
import random
asesor=input("ingrese su nombre de tienda: ")
cliente=input("ingrese el dni del cliente para la evaluacion: ")
nro_cuotas=36
monto_aprobado=0.0
#risk=random.random()
risk=0.2
print("riesgo es:" ,risk)

if risk>=0.5:
    print("Lamentablemente no contamos con ninguna oferta para usted en estos monentos")

salario=float(input("ingrese el salario del cliente: "))
propiedades=input("cuenta con propiedades S/N:")

monto_propiedad=0.0
tienePropriedades=False
if propiedades.upper() == 'S':
    hasPropriedades=True
    monto_propiedad=float(input("cual es la valuacion de la propiedad"))

if risk<=0.3:
    if hasPropriedades:
        monto_aprobado=36*0.5*salario
    else:
        pass
elif risk<=0.5:
    monto_aprobado=36*0.2*salario 

print(f"el monto aprobado es {monto_aprobado} para el cliente con dni {cliente}")
