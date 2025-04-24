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
        gr.Blocks(css="style.css")
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
            gr.Markdown("## 🌤️ **Sistema de Gestión Meteorológica**")
            gr.Markdown("### ¡Gestiona tus estaciones con estilo!")

            with gr.Row():
                gr.Markdown("### 🌧️ **Agregar Nueva Estación**")
                nombre_estacion = gr.Textbox(label="Nombre de la Estación", placeholder="Ejemplo: Lluvia")
                salida_agregar = gr.Textbox(label="Estado de la Operación")
                boton_agregar = gr.Button("Agregar Estación", elem_id="boton-agregar")

            boton_agregar.click(fn=agregar_estacion, inputs=[nombre_estacion], outputs=[salida_agregar])

            with gr.Row():
                gr.Markdown("### ☀️ **Registrar Datos Meteorológicos**")
                nombre_estacion_registro = gr.Textbox(label="Nombre de la Estación", placeholder="Ejemplo: Sol")
                datos_registro = gr.Textbox(label="Datos a Registrar", placeholder="Ejemplo: Martes 19°C")
                salida_registro = gr.Textbox(label="Estado del Registro")
                boton_registrar = gr.Button("Registrar Datos", elem_id="boton-registrar")

            boton_registrar.click(fn=registrar_datos, inputs=[nombre_estacion_registro, datos_registro], outputs=[salida_registro])

            with gr.Row():
                gr.Markdown("### 🌥️ **Consultar Datos de una Estación**")
                consulta_estacion = gr.Textbox(label="Nombre de la Estación", placeholder="Ejemplo: Nublado")
                salida_datos = gr.Textbox(label="Datos Registrados")
                boton_consultar = gr.Button("Ver Datos", elem_id="boton-consultar")

            boton_consultar.click(fn=obtener_datos, inputs=[consulta_estacion], outputs=[salida_datos])

            with gr.Row():
                gr.Markdown("### ❄️ **Guardar Datos en Archivo CSV**")
                nombre_guardar = gr.Textbox(label="Nombre de la Estación", placeholder="Ejemplo: Nevado")
                salida_guardado = gr.Textbox(label="Estado del Guardado")
                boton_guardar = gr.Button("Guardar en archivo.csv", elem_id="boton-guardar")

            boton_guardar.click(fn=self.guardar_en_csv, inputs=[nombre_guardar], outputs=[salida_guardado])

        interfaz.launch()