def calculadorImc():
    peso=50
    talla=1.5
    imc=peso/talla
    print(imc)

#calculadorImc()

# calcular el imc de todo el salon
curso_medidas={
    '9749779':{
        'peso':50,
        'talla':160
    },
    '646464':{
    'peso':70,
    'talla':170
},
    '2131231123':{
    'peso':80,
    'talla':165
},
    '123123123':{
    'peso':55,
    'talla':160
},
    '5545445':{
        'peso':50,
        'talla':160
},
    '4554542':{
    'peso':45,
    'talla':150
},
    '3443343':{
        'peso':60,
        'talla':180,
        'diasTreno':["L","M","W","S"]
    },
}
curso_medidas["3443343"]["peso"]
curso_medidas["3443343"]["talla"]
curso_medidas["3443343"]["diasTreno"][-1]



def calculadorImcv2(peso,talla):
    tallaMetros=talla/100
    return peso/tallaMetros
lista_imc=[]

for i,j in curso_medidas.items():
    #print(i,"=>",j)
    imc = calculadorImcv2(j["peso"],j["talla"])
    dictTmp={
            'dni':i,
            'imc':imc
    }
    lista_imc.append(dictTmp) 

    
for i in lista_imc:
    if i["imc"]>32:
        print(f"el cliente {i["dni"]} tiene un imc mayor a 32")


