def Menuu():
    msg="""
    BIENVENIDO A BUENOSTRENES.COM
    1.VER MIS DATOS
    2.VER RUTAS
    3.VER BUSSES
    4.SALIR
    """     
    while True:
        print(msg)
        opcion=int(input("ingrese una opcion del menu:"))
        match opcion:
            case 1:
              
               
                pass
            case 2:
                
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Hasta luego")
                break
            case _:
                print("ingrese una opcion valida")