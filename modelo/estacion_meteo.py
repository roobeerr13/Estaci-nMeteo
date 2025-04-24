import hashlib
import hmac
import os

# Función para cargar o generar la clave secreta
def cargar_o_generar_clave():
    clave_path = "clave_secreta.key"

    if not os.path.exists(clave_path):
        try:
            clave_secreta = os.urandom(32)  # Genera una clave aleatoria de 32 bytes
            with open(clave_path, "wb") as key_file:
                key_file.write(clave_secreta)
            print(f"✅ Clave secreta generada en {clave_path}")
        except Exception as e:
            print(f"❌ Error al generar la clave: {e}")
            return None
    else:
        try:
            with open(clave_path, "rb") as key_file:
                clave_secreta = key_file.read()
            print(f"🔑 Clave secreta cargada correctamente desde {clave_path}")
        except Exception as e:
            print(f"❌ Error al cargar la clave: {e}")
            return None

    return clave_secreta

CLAVE_SECRETA = cargar_o_generar_clave()

if CLAVE_SECRETA is None:
    raise RuntimeError("No se pudo generar ni cargar la clave secreta correctamente.")

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