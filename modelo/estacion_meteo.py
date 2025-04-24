import hashlib
import hmac
import os

# Verificar si el archivo de clave secreta existe, si no, generar una nueva clave
def cargar_o_generar_clave():
    if not os.path.exists("clave_secreta.key"):
        clave_secreta = os.urandom(32)  # Genera una clave aleatoria de 32 bytes
        with open("clave_secreta.key", "wb") as key_file:
            key_file.write(clave_secreta)
    else:
        with open("clave_secreta.key", "rb") as key_file:
            clave_secreta = key_file.read()
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

    def verificar_datos(self, datos):
        """Verifica si un dato ha sido registrado comparando el hash."""
        nuevo_hash = hmac.new(CLAVE_SECRETA, datos.encode(), hashlib.sha256).hexdigest()
        return nuevo_hash in self.datos_hashed