import gradio as gr

class VistaGradio:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_interfaz(self):
        def agregar_estacion(nombre):
            self.controlador.agregar_estacion(nombre)
            return f"✅ Estación '{nombre}' agregada correctamente."

        def registrar_datos(nombre, datos):
            self.controlador.registrar_datos(nombre, datos)
            return f"✅ Dato registrado en '{nombre}': {datos}"

        def verificar_datos(nombre, datos):
            resultado = self.controlador.verificar_datos(nombre, datos)
            return "✅ Dato existente en la estación." if resultado else "❌ Dato NO registrado."

        with gr.Blocks() as interfaz:
            gr.Markdown("## 🌤️ **Sistema Meteorológico con Encriptación**")

            with gr.Row():
                gr.Markdown("### 🏡 **Agregar Nueva Estación**")
                nombre_estacion = gr.Textbox(label="Nombre de la Estación", placeholder="Ejemplo: Lluvia")
                salida_agregar = gr.Textbox(label="Estado de la Operación")
                boton_agregar = gr.Button("Agregar Estación")

            boton_agregar.click(fn=agregar_estacion, inputs=[nombre_estacion], outputs=[salida_agregar])

            with gr.Row():
                gr.Markdown("### ☁️ **Registrar Datos Meteorológicos**")
                nombre_estacion_registro = gr.Textbox(label="Nombre de la Estación")
                datos_registro = gr.Textbox(label="Datos a Registrar")
                salida_registro = gr.Textbox(label="Estado del Registro")
                boton_registrar = gr.Button("Registrar Datos")

            boton_registrar.click(fn=registrar_datos, inputs=[nombre_estacion_registro, datos_registro], outputs=[salida_registro])

            with gr.Row():
                gr.Markdown("### ✅ **Verificar Datos Meteorológicos**")
                nombre_estacion_verificar = gr.Textbox(label="Nombre de la Estación")
                datos_verificar = gr.Textbox(label="Dato a Verificar")
                salida_verificar = gr.Textbox(label="Estado de la Verificación")
                boton_verificar = gr.Button("Verificar Dato")

            boton_verificar.click(fn=verificar_datos, inputs=[nombre_estacion_verificar, datos_verificar], outputs=[salida_verificar])

        interfaz.launch()