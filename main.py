from modelo.estacion_meteo import EstacionMeteorologica
from controlador.controlador import Controlador
from vista.vista_gradio import VistaGradio

# Inicialización
estacion = EstacionMeteorologica("Estación Central")
controlador = Controlador(estacion)
vista = VistaGradio(controlador)

# Ejecutar la interfaz
vista.mostrar_interfaz()