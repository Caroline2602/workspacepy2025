#PRIMERA ACTIVIDAD#
print("HOLA MUNDO")
#SEGUNDA ACTIVIDAD#
nombreUsuario = input("Por favor, ingresa tu nombre: ")
print("¡Hola " + nombreUsuario + "!")
#TERCERA ACTIVIDAD#
edadUsuario = int(input("Por favor, ingresa tu edad: "))
if edadUsuario >= 18:
    print(f"EDAD:  {edadUsuario}  ERES MAYOR DE EDAD");
else:
    print(f"EDAD: {edadUsuario}  ERES MENOR DE EDAD")
#CUARTA ACTIVIDAD#
numeroEntero=int(input("INGRESE UN NÚMERO: "))
if  numeroEntero>=0 and numeroEntero % 2 ==0:
    print(f"EL NUMERO INGRESADO {numeroEntero} ES PAR Y POSITIVO");
if  numeroEntero<0 and numeroEntero % 2 ==0:
    print(f"EL NUMERO INGRESADO {numeroEntero} ES PAR Y NEGATIVO");
if  numeroEntero>0 and numeroEntero % 2!=0:
    print(f"EL NUMERO INGRESADO {numeroEntero} ES IMPAR Y POSITIVO");
if numeroEntero<0 and numeroEntero%2!=0:
    print(f"EL NUMERO INGRESADO {numeroEntero} ES IMPAR Y NEGATIVO")
#QUINTA ACTIVIDAD#
Numero=input("Por favor ingrese un número entero: ")
if "." in Numero:
    print("NO ES UN NUMERO ENTERO");
else:
    suma=(abs((int(Numero))) * (abs((int(Numero))) + 1))/ 2;
    print(f"TOTAL: {suma}");