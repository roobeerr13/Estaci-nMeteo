class Controlador:
    def __init__(self, sistema_meteorologico):
        self.sistema_meteorologico = sistema_meteorologico

    def agregar_estacion(self, nombre):
        self.sistema_meteorologico.agregar_estacion(nombre)

    def registrar_datos(self, nombre, datos):
        self.sistema_meteorologico.registrar_datos_estacion(nombre, datos)

    def obtener_datos(self, nombre):
        return self.sistema_meteorologico.obtener_datos_estacion(nombre)