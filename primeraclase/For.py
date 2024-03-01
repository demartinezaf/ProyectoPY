
# Recorrer listas - tuplas y diccionarios

# Data type is list
data_list = [1,2,3,4,5]
print(type(data_list))

# Data type is tuple
data_tuple = ("juan", "Perez", 25)
print(type(data_tuple), data_tuple)

# Data type is dictionary
data_dictionary = {
    "a": 1,
    "b": 2,
    "c": "nombre",
    "d": True
}

for i in data_list:
    if i == 3:
        print(i)


for j in data_tuple:
    if j == "juan":
        print(f"Nombre {j}")
    elif j == "Perez":
        print(f"Apellido {j}")
    elif j == 25:
        print(f"Edad {j}")


for clave,valor in data_dictionary.items():
    print(f"clave {clave},valor {valor}")

for i in data_dictionary:
    if i == 'a':
        j = data_dictionary[i]
        print(j)

