print("=====================================")
print("Comprobador de numeros par o impar :)")
print("=====================================\n")

num=input(int("Introduce un NUMERO ENTERO por favor uwu:\n"))

if num % 2 == 0:
    print("El numero ",num," es par")
elif num % 2 != 0:
    print("El numero ",num," es inpar")
else:
    print("El dato",str(num)," no es válido")
