import gradio as gr

class VistaGradio:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_interfaz(self):
        def agregar_estacion(nombre):
            self.controlador.agregar_estacion(nombre)
            return f"Estación '{nombre}' agregada correctamente."

        def registrar_datos(nombre, datos):
            self.controlador.registrar_datos(nombre, datos)
            return f"Dato registrado en '{nombre}': {datos}"

        def obtener_datos(nombre):
            datos = self.controlador.obtener_datos(nombre)
            return "\n".join(datos) if datos else "No hay datos para esta estación."

        interfaz_agregar = gr.Interface(
            fn=agregar_estacion,
            inputs="text",
            outputs="text",
            title="Agregar Nueva Estación Meteorológica"
        )

        interfaz_registro = gr.Interface(
            fn=registrar_datos,
            inputs=["text", "text"],
            outputs="text",
            title="Registrar Datos Meteorológicos"
        )

        interfaz_visualizacion = gr.Interface(
            fn=obtener_datos,
            inputs="text",
            outputs="text",
            title="Ver Datos de una Estación"
        )

        gr.TabbedInterface(
            [interfaz_agregar, interfaz_registro, interfaz_visualizacion],
            ["Agregar Estación", "Registrar Datos", "Ver Datos"]
        ).launch()