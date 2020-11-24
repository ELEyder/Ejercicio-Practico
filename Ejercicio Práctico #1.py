Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
   L1  L2  L3
R1   |   |     
   ---------
R2   | X |  
   ---------
R3   |   |   
¿Que fila L elijes?¿1, 2, o 3?
4
Este valor no puede ser elegido, revisa las opciones
   L1  L2  L3
R1   |   |     
   ---------
R2   | X |  
   ---------
R3   |   |   
¿Que fila L elijes?¿1, 2, o 3?
1
¿Que fila R elijes?¿1, 2, o 3?
1
   L1  L2  L3
R1 O |   |     
   ---------
R2   | X |  
   ---------
R3   |   |   
¿Que fila L elijes?¿1, 2, o 3?
1
¿Que fila R elijes?¿1, 2, o 3?
1
   L1  L2  L3
R1 O |   |     
   ---------
R2   | X |  
   ---------
R3   |   |   
¿Que fila L elijes?¿1, 2, o 3?

Traceback (most recent call last):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 38, in <module>
    juego()
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 22, in juego
    filaL=int(input("¿Que fila L elijes?¿1, 2, o 3?\n"))
ValueError: invalid literal for int() with base 10: ''
1
>>> 1
1
1
>>> 
>>> 
>>> 
>>> 
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
Traceback (most recent call last):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 4, in <module>
    tablero= [fila][columna]
NameError: name 'fila' is not defined
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
Traceback (most recent call last):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 4, in <module>
    tablero= [fila][columna]
NameError: name 'fila' is not defined
>>> 
Warning (from warnings module):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 4
    tablero= [1,2,3][1,2,3]
SyntaxWarning: list indices must be integers or slices, not tuple; perhaps you missed a comma?
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
Traceback (most recent call last):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 4, in <module>
    tablero= [1,2,3][1,2,3]
TypeError: list indices must be integers or slices, not tuple
>>> 
Warning (from warnings module):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 4
    tablero= [[1,2,3][4,x,6][7,8,9]]
SyntaxWarning: list indices must be integers or slices, not tuple; perhaps you missed a comma?
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
Traceback (most recent call last):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 4, in <module>
    tablero= [[1,2,3][4,x,6][7,8,9]]
NameError: name 'x' is not defined
>>> 
Warning (from warnings module):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 4
    tablero= [[1,2,3][4,"x",6][7,8,9]]
SyntaxWarning: list indices must be integers or slices, not tuple; perhaps you missed a comma?
>>> 

======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
>>> 
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
Traceback (most recent call last):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 4, in <module>
    tablero= [[1,2,3][4,"x",6][7,8,9]]
TypeError: list indices must be integers or slices, not tuple
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
[[1, 2, 3], [4, 'x', 6], [7, 8, 9]]
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
[4, 'x', 6]
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
x
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
Traceback (most recent call last):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 6, in <module>
    for i in range(tablero):
TypeError: 'list' object cannot be interpreted as an integer
>>> 
======= RESTART: C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py ======
Bienvenido a el famoso juego: "¡Tres en raya!"
Pulsa ENTER para continuar
Traceback (most recent call last):
  File "C:\Users\2020\Documents\Practicas PHYTON\Tres en Raya.py", line 6, in <module>
    for i in range(tablero):
TypeError: 'list' object cannot be interpreted as an integer
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado?Eyder
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? Eyder
Traceback (most recent call last):
  File "C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py", line 3, in <module>
    calve=input("¿Cual es tu clave de departamento?", nombre)
TypeError: input expected at most 1 argument, got 2
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? 
¿Cual es tu clave de departamento?
>>> 
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? Eyder
¿Cual es tu clave de departamento?Eyder
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? Eyder
¿Cual es tu clave de departamento? Eyder
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? Eyder
¿Cual es tu clave de departamento? Eyder 1
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? Eyder
Eyder, ¿Cual es tu clave de departamento? 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? 
Eyder
Eyder, ¿Cual es tu clave de departamento? 
1
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? 
Eyder
Eyder, ¿Cual es tu clave de departamento? 
1
¿Cuántos años tienes trabajando?1
Usuario Eyder .Usted recibirá 6 días de vacaciones
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? 
Eyder
Eyder, ¿Cual es tu clave de departamento? 
4
¿Cuántos años tienes trabajando?
1
La clave. 4  no existe
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? 
Eyder
Eyder, ¿Cual es tu clave de departamento? 
5
¿Cuántos años tienes trabajando?
1
La clave  5  no existe
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
Días de vacaciones segun tus años trabajados
¿Cuál es el nombre del empleado? 
Eyder
Eyder, ¿Cual es tu clave de departamento? 
2
¿Cuántos años tienes trabajando?
10
Usuario Eyder .Usted recibirá 22 días de vacaciones
>>> 
= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
--------------------------------------------
Días de vacaciones segun tus años trabajados
--------------------------------------------
¿Cuál es el nombre del empleado? 

= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
--------------------------------------------
Días de vacaciones segun tus años trabajados
--------------------------------------------

¿Cuál es el nombre del empleado? 

= RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py
--------------------------------------------
Días de vacaciones segun tus años trabajados
--------------------------------------------

¿Cuál es el nombre del empleado? 
Eyder
Eyder, ¿Cual es tu clave de departamento? 
2
¿Cuántos años tienes trabajando?
5
Usuario Eyder .Usted recibirá 15 días de vacaciones
>>> 

>>> 
>>> 
==== RESTART: C:/Users/2020/AppData/Local/Programs/Python/Python38/Práctica Propuesta.py ===
--------------------------------------------
Días de vacaciones segun tus años trabajados
--------------------------------------------

¿Cuál es el nombre del empleado? 
Eyder
Eyder, ¿Cual es tu clave de departamento? 
1
¿Cuántos años tienes trabajando?
7
Usuario Eyder .Usted recibirá 20 días de vacaciones
>>> 