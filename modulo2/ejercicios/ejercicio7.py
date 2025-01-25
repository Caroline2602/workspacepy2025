def calculoImpuesto(monto,igv=0.18):
    return monto*igv


def calculoTasa():
    regimen=input("que regimen desea calcular")
    if regimen=='1':
        return 0.05
    
salario=float(input("ingrese su salario"))
tasa=calculoTasa()
print(tasa)
impuesto=None
if tasa:
    print("la tasa existe")
    impuesto=calculoImpuesto(salario,tasa)
else:
    impuesto=calculoImpuesto(salario)

print(f"el impuesto para su salario {salario} es {impuesto}")