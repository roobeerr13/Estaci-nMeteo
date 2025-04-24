from cryptography.fernet import Fernet

try:
    with open("key.key", "rb") as key_file:
        key = key_file.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

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