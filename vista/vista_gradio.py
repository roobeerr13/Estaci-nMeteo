import gradio as gr
import csv

class VistaGradio:
    def __init__(self, controlador):
        self.controlador = controlador

    def guardar_en_csv(self, nombre):
        datos = self.controlador.obtener_datos(nombre)
        if not datos:
            return f"No hay datos para la estación '{nombre}'."

        with open("datos_meteorologicos.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([nombre] + datos)

        return f"Datos de '{nombre}' guardados en archivo CSV."

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

        with gr.Blocks() as interfaz:
            gr.Markdown("## 🌤️ Sistema de Gestión Meteorológica")

            with gr.Row():
                nombre_estacion = gr.Textbox(label="Nombre de la Estación")
                datos_registro = gr.Textbox(label="Registro de Datos")
                boton_registrar = gr.Button("Registrar Datos")

            boton_registrar.click(fn=registrar_datos, inputs=[nombre_estacion, datos_registro], outputs="text")

            with gr.Row():
                consulta_estacion = gr.Textbox(label="Consultar Estación")
                boton_consultar = gr.Button("Ver Datos")

            boton_consultar.click(fn=obtener_datos, inputs=[consulta_estacion], outputs="text")

            with gr.Row():
                nombre_guardar = gr.Textbox(label="Guardar Datos de la Estación")
                boton_guardar = gr.Button("Guardar en archivo.csv")

            boton_guardar.click(fn=self.guardar_en_csv, inputs=[nombre_guardar], outputs="text")

        interfaz.launch()