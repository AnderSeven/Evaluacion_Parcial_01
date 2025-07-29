empleados = {}
class Empleado:
    def __init__(self, codigo, nombre, departamento, antiguedad):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad

class Evaluacion:
    def __init__(self, puntualidad, trabajo_equipo, productividad):
        self.puntualidad = puntualidad
        self.trabajo_equipo = trabajo_equipo
        self.pruductividad = productividad

class InformacionContacto:
    def __init__(self, telefono, correo):
        self.telefono = telefono
        self.correo = correo

def registro():
    x = 0
    cantidad = int(input("Cuantos empleados desea registrar: "))
    for i in range(cantidad):
        nombre = input(f"\nIngrese el nombre del empleado {x+1}: ")
        codigo = int(input("Ingerse el codigo: "))
        departamento = input("Ingrese el departamento: ")
        antiguedad = int(input("Ingrese la antiguedad: "))
        empleados = {
            nombre: 'nombre'

        }

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
            print("asdf")
        case 2:
            print("asdf")
        case 3:
            print("adsf")
        case 4:
            print("asdf")
        case 5:
            print("Gracias por usar el sistema")
        case _:
            print("Opcion invalida")