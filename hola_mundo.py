# 1. TAREA: imprime "Hola, mundo"
print('Hola, mundo')
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Noelle"
print('Hola, ' + name + ',')	# con una coma
print('Hola, ' + name + '+')	# con un +

#2 a
name= "Amanda"
print('¡Hola, ' + str(name) + '!')
#2 b
print('¡Hola, ' + str(name) + '+' + '!')
# 3. imprimir "Hola 42!" con el número en una variable
#3 corregido

age = 42
print('Hola, '+ str(age) + '!')	# con una coma
print('Hola, ' + str(age) + '+')	# con una +	-- este debería arrojar un error!

#3a

num= 6
print('¡Hola, ' + str(num) + ',' + '!')

#3b
print('¡Hola, ' + str(num) + '+' + '!')


# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer {} y {}" .format(fave_food1, fave_food2)) # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f

#4 a
comida_uno = "lasaña"
comida_dos = "tacos"

print("Amo comer {} y {}" .format(comida_uno, comida_dos))

#4b

print(f"Amo comer {comida_uno} y {comida_dos}")

