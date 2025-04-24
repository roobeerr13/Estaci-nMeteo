from modelo.estacion_meteo import SistemaMeteorologico
from controlador.controlador import Controlador
from vista.vista_gradio import VistaGradio

# Inicialización con estaciones meteorológicas predefinidas
sistema_meteorologico = SistemaMeteorologico()
controlador = Controlador(sistema_meteorologico)
vista = VistaGradio(controlador)

# Lanzar la interfaz con diseño mejorado
vista.mostrar_interfaz()