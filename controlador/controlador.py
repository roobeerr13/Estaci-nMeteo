class Controlador:
    def __init__(self, sistema_meteorologico):
        self.sistema_meteorologico = sistema_meteorologico

    def agregar_estacion(self, nombre):
        self.sistema_meteorologico.agregar_estacion(nombre)

    def registrar_datos(self, nombre, datos):
        self.sistema_meteorologico.registrar_datos_estacion(nombre, datos)

    def verificar_datos(self, nombre, datos):
        return self.sistema_meteorologico.verificar_datos_estacion(nombre, datos)