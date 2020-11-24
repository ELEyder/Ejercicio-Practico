print("--------------------------------------------")
print("Días de vacaciones segun tus años trabajados")
print("--------------------------------------------\n")

nombre=input("¿Cuál es el nombre del empleado? \n")
clave=int(input(nombre + ", ¿Cual es tu clave de departamento? \n"))
años=int(input("¿Cuántos años tienes trabajando?\n"))
if clave == 1: 
    if años == 1:
        print("Usuario",nombre,".Usted recibirá 6 días de vacaciones")
    elif años >= 2 and años <=6:
        print("Usuario",nombre,".Usted recibirá 14 días de vacaciones")
    elif años >=7:
        print("Usuario",nombre,".Usted recibirá 20 días de vacaciones")
    else:
        print("Sin derecho a vacaciones")
elif clave == 2:
    if años == 1:
        print("Usuario",nombre,".Usted recibirá 7 días de vacaciones")
    elif años >= 2 and años <=6:
        print("Usuario",nombre,".Usted recibirá 15 días de vacaciones")
    elif años >=7:
        print("Usuario",nombre,".Usted recibirá 22 días de vacaciones")
    else:
        print("Sin derecho a vacaciones")
elif clave == 3:
    if años == 1:
        print("Usuario",nombre,".Usted recibirá 10 días de vacaciones")
    elif años >= 2 and años <=6:
        print("Usuario",nombre,".Usted recibirá 20 días de vacaciones")
    elif años >=7:
        print("Usuario",nombre,".Usted recibirá 30 días de vacaciones")
    else:
        print("Sin derecho a vacaciones")
else:
    print("La clave ",clave," no existe")
