import hashlib
import hmac

CLAVE_SECRETA = b"clave_secreta_segura"

class EstacionMeteorologica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos_hashed = []

    def registrar_datos(self, datos):
        """Genera un hash usando HMAC con la clave secreta y lo almacena."""
        hashed_data = hmac.new(CLAVE_SECRETA, datos.encode(), hashlib.sha256).hexdigest()
        self.datos_hashed.append(hashed_data)

    def verificar_datos(self, datos):
        """Verifica si un dato ha sido registrado comparando el hash."""
        nuevo_hash = hmac.new(CLAVE_SECRETA, datos.encode(), hashlib.sha256).hexdigest()
        return nuevo_hash in self.datos_hashed

class SistemaMeteorologico:
    def __init__(self):
        self.estaciones = {}

        # Estaciones meteorológicas predefinidas
        estaciones_predefinidas = ["Lluvia", "Sol", "Nublado", "Nevado", "Tormenta", "Neblina", "Viento fuerte"]
        for nombre in estaciones_predefinidas:
            self.agregar_estacion(nombre)

    def agregar_estacion(self, nombre):
        """Registra una nueva estación meteorológica."""
        if nombre not in self.estaciones:
            self.estaciones[nombre] = EstacionMeteorologica(nombre)

    def registrar_datos_estacion(self, nombre, datos):
        """Registra un dato meteorológico en la estación."""
        if nombre in self.estaciones:
            self.estaciones[nombre].registrar_datos(datos)

    def verificar_datos_estacion(self, nombre, datos):
        """Verifica si un dato existe en la estación."""
        if nombre in self.estaciones:
            return self.estaciones[nombre].verificar_datos(datos)
        return False