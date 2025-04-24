from modelo.estacion_meteo import SistemaMeteorologico
from controlador.controlador import Controlador
from vista.vista_gradio import VistaGradio

# Inicialización del sistema meteorológico
sistema_meteorologico = SistemaMeteorologico()
controlador = Controlador(sistema_meteorologico)
vista = VistaGradio(controlador)

# Lanzar la interfaz gráfica
vista.mostrar_interfaz()