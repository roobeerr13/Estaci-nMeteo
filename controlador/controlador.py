class Controlador:
    def __init__(self, modelo):
        self.modelo = modelo

    def agregar_datos(self, datos):
        self.modelo.registrar_datos(datos)

    def obtener_datos(self):
        return self.modelo.obtener_datos()