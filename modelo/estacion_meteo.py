from cryptography.fernet import Fernet

def cargar_o_generar_clave():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
            if len(key) != 44:  # La clave debe tener exactamente 44 caracteres en base64
                raise ValueError("Clave incorrecta, regenerando...")
    except (FileNotFoundError, ValueError):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    return key

key = cargar_o_generar_clave()
cipher_suite = Fernet(key)

class EstacionMeteorologica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos_encriptados = []

    def registrar_datos(self, datos):
        encrypted_data = cipher_suite.encrypt(datos.encode())
        self.datos_encriptados.append(encrypted_data)

    def obtener_datos(self):
        return [cipher_suite.decrypt(d).decode() for d in self.datos_encriptados]

class SistemaMeteorologico:
    def __init__(self):
        self.estaciones = {}

        estaciones_predefinidas = ["Lluvia", "Sol", "Nublado", "Nevado", "Tormenta", "Neblina", "Viento fuerte"]
        for nombre in estaciones_predefinidas:
            self.agregar_estacion(nombre)

    def agregar_estacion(self, nombre):
        if nombre not in self.estaciones:
            self.estaciones[nombre] = EstacionMeteorologica(nombre)

    def registrar_datos_estacion(self, nombre, datos):
        if nombre in self.estaciones:
            self.estaciones[nombre].registrar_datos(datos)

    def obtener_datos_estacion(self, nombre):
        if nombre in self.estaciones:
            return self.estaciones[nombre].obtener_datos()
        return []