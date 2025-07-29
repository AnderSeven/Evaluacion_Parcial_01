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

