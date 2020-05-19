def menu():
	print("\n" * 50) 

	print("\t\t*** MENU ***\n")
	print("\t1. Sum")
	print("\t2. Subtraction")
	print("\t3. Multiplication")
	print("\t4. Division")
	print("\t5. Result")
	print("\t0. Exit")

def opcion(min, max, salida):
	opcion= -1
	
	menu() 
	opcion= int(input("\n\t-> Opcion?: ")) 

	while (opcion < min) or (opcion > max):
		print("\n\t>>> Error. Opcion invalida.")
		print("\t    Presione una tecla para continuar ...")
		input()
		
		menu() 
		opcion= int(input("\n\t-> Opcion?: ")) 
	
	return opcion
		
def submenu(titulo):
	print("\n" * 50) 
	print("\t\t*** " + titulo.upper() + " ***\n")


def fSuma():
	submenu("SUMA")
	num1 = float(input("\tIngrese un numero: "))
	num2 = float(input("\tIngrese un numero: "))
	
	respuesta = num1 + num2
	
	
	print("\n\t-> El resultado de " + str(num1) + " + " + str(num2) + "= ", respuesta)
	print("\t   Presione cualquier tecla para continuar ...")
	input()
	return respuesta
	

def fResta():
	submenu("RESTA")
	num1 = float(input("\tIngrese un numero: "))
	num2 = float(input("\tIngrese un numero: "))
	
	respuesta = num1 - num2
	
	
	print("\n\t-> El resultado de " + str(num1) + " - " + str(num2) + "= ", respuesta)
	print("\t   Presione cualquier tecla para continuar ...")
	input()
	return respuesta
	

def fMultiplicacion():
	submenu("MULTIPLICACION")
	num1 = float(input("\tIngrese un numero: "))
	num2 = float(input("\tIngrese un numero: "))
	
	respuesta = num1 * num2
	

	print("\n\t-> El resultado de " + str(num1) + " * " + str(num2) + "= ", respuesta)
	print("\t   Presione cualquier tecla para continuar ...")
	input()
	return respuesta
	

def fDivision():
	submenu("division") 
	num1 = float(input("\tIngrese un dividendo: "))
	num2 = float(input("\tIngrese un divisor: "))
	
	if num2 != 0:
		respuesta = num1 / num2
	

		print("\n\t-> El resultado de " + str(num1) + " / " + str(num2) + "= ", respuesta)
	else:
		#Division entre cero
		print("\n\t>>> Error. Division entre cero.")
		respuesta= "Error. Division entre cero."
		
	print("\t   Presione cualquier tecla para continuar ...")
	input()
	return respuesta
	
#funcion que muesta el ultimo resultado calculado
def fResultado(r):
	submenu("resultado") #no importa enviarlo en minuscula submenu la convierte
	
	print("\n\t-> El ultimo resultado calculado fue: " , r)
	print("\t    Presione cualquier tecla para continuar ...")
	input()
	
def fSalida():
	submenu("Salida") #no importa enviarlo en minuscula submenu la convierte
	
	print("\n\t-> Gracias por usarnos. Adios.  ")
	print("\t   Presione cualquier tecla para terminar ...")
	input()
	print("\n" * 60) #varios cambios de lineas con el fin de limpiar la pantalla




#*************************
#*** PROGRAMA PRINCIAL ***
#*************************

resultado = 0
op= -1

while op != 0:
	op = opcion(0, 5, 0) #call option fccion
	
	if op == 1:
		## funcion Suma
		resultado = fSuma()
		
	elif op == 2:
		## funcion Resta
		resultado = fResta()
		
	elif op == 3:
		## funcion Multiplicacion
		resultado = fMultiplicacion()
		
	elif op == 4:
		## funcion Division
		resultado = fDivision()
	elif op == 5:
		## funcion Resultado
		fResultado(resultado)
	else:
		## funcion Salida
		resultado = fSalida()
