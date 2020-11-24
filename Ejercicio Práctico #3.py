print("El número Mayor")
num1=int(input("Ingrese el primer número por favor"))
num2=int(input("Ingrese el segundo número por favor"))
num3=int(input("Ingrese el último número por favor"))
if num1 > num2 and num1 > num3:
    print("El número ",num1," es el mayor")
else:
    if num2 > num3:
        print("El número ",num2," es el mayor")
    else:
        print("El número ",num3," es el mayor")

