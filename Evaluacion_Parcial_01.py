empleados = {}
class Empleado:
    def __init__(self, codigo, nombre, departamento, antiguedad):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad

class Evaluacion:
    def __init__(self, puntualidad, trabajo_equipo, productividad, observaciones):
        self.puntualidad = puntualidad
        self.trabajo_equipo = trabajo_equipo
        self.pruductividad = productividad
        self.observaciones = observaciones

class InformacionContacto:
    def __init__(self, telefono, correo):
        self.telefono = telefono
        self.correo = correo

def registro():
    x = 0
    cantidad = int(input("Cuantos empleados desea registrar: "))
    for i in range(cantidad):
        x += 1
        nombre = input(f"\nIngrese el nombre del empleado {x}: ")
        a = False
        while a == False:
            codigo = int(input("Ingerse el ID: "))
            if codigo in empleados:
                print("codigo invalido")
            else:
                a = True
        departamento = input("Ingrese el departamento: ")
        antiguedad = int(input("Ingrese la antiguedad: "))
        empleados[codigo] = {
            'nombre': nombre,
            'departamento': departamento,
            'antiguedad': antiguedad,
            'evaluacion':{}
        }
        a = Empleado(nombre, codigo, departamento, antiguedad)
        print("\n----Evaluacion----")
        print("Califique del 1 al 10")
        s = False
        while s == False:
            puntuabilidad = float(input("Califique la puntuabilidad: "))
            if puntuabilidad >= 0 and puntuabilidad <= 10:
                s = True
            else:
                print("Calificacion invalida")
        s = False
        while s == False:
            trabajo_equipo = float(input("Califique el trabajo en equipo: "))
            if trabajo_equipo >= 0 and trabajo_equipo <= 10:
                s = True
            else:
                print("Calificacion invalida")
        s = False
        while s == False:
            productividad = float(input("Califique la productividad: "))
            if productividad >= 0 and productividad <= 10:
                s = True
            else:
                print("Calificacion invalida")
        observacion = input("Ingrese las observaciones: ")
        promedio = (puntuabilidad + trabajo_equipo + productividad) / 3
        if promedio >= 7:
            print(f"\nPromedio del empleado: {promedio}")
            print("Desempeño: Satisfactorio")
            estado = "Satisfactorio"
        else:
            print(f"\nPromedio del empleado: {promedio}")
            print("Desempeño: Debe mejorar")
            estado = "Debe mejorar"
        empleados[codigo]['evaluacion'] = {
            'puntuabilidad': puntuabilidad,
            'trabajo_equipo': trabajo_equipo,
            'productividad': productividad,
            'observacion': observacion,
            'promedio': promedio,
            'estado': estado,
            'contacto': {}
        }
        telefono = int(input("Ingrese el numero de telefono: "))
        correo = input("Ingrese el correo electronico: ")
        empleados[codigo]['evaluacion']['contacto'] = {
            'telefono': telefono,
            'correo': correo
        }
        print("\nSe ha registrado al empleado con exito")

def buscar():
    if len(empleados) > 0:
        print("----Buscar empleados----")
        codigo = int(input("Ingrese el codigo del empleado: "))
        if codigo in empleados:
            print(f"Nombre: {empleados[codigo]['nombre']}, Departamento: {empleados[codigo]['departamento']}, Antiguedad: {empleados[codigo]['antiguedad']}")
        else:
            print("No hay ningun empleado con ese codigo")
    else:
        print("No hay empleados registrados")

opciones = 0
a = False
while a == False:
    print("----Menu----")
    print("1. Registro de usuario")
    print("2. Buscar empleado por ID")
    print("3. Mostrar cuantos empleados tiene evaluacion satisfactoria")
    print("4. Empleado con mejor promedio general")
    print("5. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            registro()
        case 2:
            buscar()
        case 3:
            print("adsf")
        case 4:
            print("asdf")
        case 5:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")