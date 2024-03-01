#Tarea

grade = int(input("Insert grade"))

if 90 <= grade <= 100:
    print("Excelente")
elif 80 <= grade <= 89:
    print("Bien")
elif 70 <= grade <= 79:
    print("Regular")
elif 0 <= grade <= 69:
    print("No aprobado")
else:
    print("Nota no válida")

