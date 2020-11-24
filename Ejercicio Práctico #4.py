print("+++++++++++++++++++++++++++++++++")
print("Calculadora con una sola variable")
print("+++++++++++++++++++++++++++++++++\n")

numero=0
print("--------------------")
print("Menú de opciones :)")
print("--------------------\n")
numero=int(input("1.Suma\n2.Resta\n3.Multiplicación\n4.División\n5.División entera\n6.Potenciación\n7.Módulo o Resto\n"))
if numero == 1:
    numero=int(input("Dame el primer número:\n"))
    numero+=int(input("Dame el segundo número:\n"))
    print("La suma es igual a ",numero)
    
elif numero == 2:
    numero=int(input("Dame el primer número:\n"))
    numero-=int(input("Dame el segundo número:\n"))
    print("La resta es igual a ",numero)
elif numero == 3:
    numero=int(input("Dame el primer número:\n"))
    numero*=int(input("Dame el segundo número:\n"))
    print("La multiplicación es igual a ",numero)
elif numero == 4:
    numero=int(input("Dame el primer número:\n"))
    numero/=int(input("Dame el segundo número:\n"))
    print("La división es igual a ",numero)
elif numero == 5:
    numero=int(input("Dame el primer número:\n"))
    numero//=int(input("Dame el segundo número:\n"))
    print("La división exacta es igual a ",numero)
elif numero == 6:
    numero=int(input("Dame el primer número:\n"))
    numero**=int(input("Dame el segundo número:\n"))
    print("La potencia es igual a ",numero)
elif numero == 7:
    numero=int(input("Dame el primer número:\n"))
    numero%=int(input("Dame el segundo número:\n"))
    print("El residuo es igual a ",numero)
else:
    print("Esta opción no esta disponible")

