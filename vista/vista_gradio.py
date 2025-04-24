import gradio as gr

class VistaGradio:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_interfaz(self):
        def registrar_datos(datos):
            self.controlador.agregar_datos(datos)
            return f"Dato registrado: {datos}"

        def obtener_datos():
            datos = self.controlador.obtener_datos()
            return "\n".join(datos)

        interfaz_registro = gr.Interface(
            fn=registrar_datos,
            inputs="text",
            outputs="text",
            title="Registro de Datos Meteorológicos"
        )

        interfaz_visualizacion = gr.Interface(
            fn=obtener_datos,
            inputs=None,
            outputs="text",
            title="Visualización de Datos Meteorológicos",
            live=True
        )

        gr.TabbedInterface([interfaz_registro, interfaz_visualizacion], ["Registrar Datos", "Ver Datos"]).launch()