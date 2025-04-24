import hashlib
import hmac
import os
import csv

# Función para cargar o generar la clave secreta
def cargar_o_generar_clave():
    clave_path = "clave_secreta.key"

    if not os.path.exists(clave_path):
        clave_secreta = os.urandom(32)  # Genera una clave aleatoria de 32 bytes
        with open(clave_path, "wb") as key_file:
            key_file.write(clave_secreta)
        print(f"✅ Clave secreta generada en {clave_path}")
    else:
        with open(clave_path, "rb") as key_file:
            clave_secreta = key_file.read()
        print(f"🔑 Clave secreta cargada correctamente desde {clave_path}")

    return clave_secreta

CLAVE_SECRETA = cargar_o_generar_clave()

class EstacionMeteorologica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos_hashed = []

    def registrar_datos(self, datos):
        """Genera un hash con HMAC usando la clave secreta y lo almacena."""
        hashed_data = hmac.new(CLAVE_SECRETA, datos.encode(), hashlib.sha256).hexdigest()
        self.datos_hashed.append(hashed_data)

        # Guardar automáticamente en CSV
        self.guardar_en_csv(datos)

    def verificar_datos(self, datos):
        """Verifica si un dato ha sido registrado comparando el hash."""
        nuevo_hash = hmac.new(CLAVE_SECRETA, datos.encode(), hashlib.sha256).hexdigest()
        return nuevo_hash in self.datos_hashed

    def guardar_en_csv(self, datos):
        """Guarda los datos en un archivo CSV."""
        with open("datos_meteorologicos.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([self.nombre, datos])

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
        """Registra un dato meteorológico en la estación y lo guarda en CSV."""
        if nombre in self.estaciones:
            self.estaciones[nombre].registrar_datos(datos)

    def verificar_datos_estacion(self, nombre, datos):
        """Verifica si un dato existe en la estación."""
        if nombre in self.estaciones:
            return self.estaciones[nombre].verificar_datos(datos)
        return False