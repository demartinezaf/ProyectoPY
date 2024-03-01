#While

#Imprimir los números del 1 al 5

contador = 1

while contador <=7:
    print(contador)
    contador += 1

#Ingresar un número positivo

dato = int(input("Ingresa un número"))

while dato <= 0:
    print("Error. Ingrese otro número")
    dato = int(input("Número Positivo"))
print(f"Ingresaste un número positivo {dato}")

#Si el contador es igual a 3 imprimir "casi llegas". Si es menor a 5, que pueda seguir ejecutando.

contador = 0

while contador <= 5:
    print(contador)
    contador += 1
    if contador == 3:
        print("casi llegas")


