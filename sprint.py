
diccionario = {'id': [0, 1, 2, 3], 'nombre': ['Manuel', 'Patricia', 'Maria', 'Carla'], 'apellido': ['Diaz', 'Guerra', 'Flash', 'Rivas'], 'edad':[22, 25, 30, 31], 'contraseña':[1235, 541, 784, 7452]}

def agre():
    num = int(input("Ingrese numero de clientes nuevos"))
    for i in range(num):
        i = input("Ingrese Id del cliente: ")
        diccionario['id'].append(i)
        no = input("Ingrese nombre del cliente: ")
        diccionario['nombre'].append(no)
        ap = input("Ingrese el apellido del cliente: ")
        diccionario['apellido'].append(ap)
        ed = input("Ingrese la edad del cliente: ")
        diccionario['edad'].append(ed)
        con = input("Ingrese contraseña: ")
        diccionario['contraseña'].append(con)
agre()
print(diccionario)

def eli():
    num1 = int(input("¡Cuantos clientes desea eliminar?: "))
    for j in range(num1):
        re = input("Ingrese el id del cliente a eliminar")
        diccionario['id'].remove(re)
        diccionario['nombre'].pop(re)
        diccionario['apellido'].pop(re)
        diccionario['edad'].pop(re)
        diccionario['contraseña'].pop(re)
eli()
print(diccionario)
