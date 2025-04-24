# Estaci-nMeteo
https://github.com/roobeerr13/Estaci-nMeteo.git
# 🌤️ Sistema de Gestión Meteorológica con Encriptación HMAC

## 📌 Descripción
Este sistema permite **registrar y verificar datos meteorológicos de manera segura**, utilizando **HMAC-SHA256** para la protección de datos.  
El proyecto está organizado con el modelo **Vista-Controlador**, permitiendo una estructura clara y modular.  
La interfaz gráfica está diseñada con **Gradio**, ofreciendo una experiencia **intuitiva y atractiva**.

---

## Características Principales
✅ **Modelo-Vista-Controlador (MVC)** para una organización estructurada.  
✅ **Encriptación segura con HMAC-SHA256**, garantizando integridad en los datos.  
✅ **Interfaz visual con Gradio**, haciendo la interacción más sencilla.  
✅ **Lista automática de estaciones meteorológicas predefinidas**, incluyendo:
   - 🌧️ Lluvia  
   - ☀️ Sol  
   - 🌥️ Nublado  
   - ❄️ Nevado  
   - ⛈️ Tormenta  
   - 🌫️ Neblina  
   - 💨 Viento fuerte  
✅ **Validación de registros encriptados**, permitiendo verificar la autenticidad de los datos.  
✅ **Funcionalidad para guardar registros en archivo CSV**, asegurando disponibilidad futura.  

---

## 📂 Estructura del Proyecto
/EstacionMeteo/ ├── modelo/ │   └── estacion_meteorologica.py  # Manejador de datos y encriptación con HMAC ├── vista/ │   └── vista_gradio.py  # Interfaz gráfica interactiva con Gradio ├── controlador/ │   └── controlador.py  # Gestión entre modelo y vista ├── main.py  # Archivo principal que conecta todo ├── requirements.txt  # Dependencias del proyecto ├── README.md  # Documentación del proyecto └── .gitignore  # Archivos a excluir en el repositorio


## Instalar dependencias: 
pip install -r requirements.txt

## Ejecutar 
python main.py

## Seguridad
Este sistema usa HMAC-SHA256 para proteger los registros meteorológicos.
Cada dato ingresado es cifrado con una clave secreta (CLAVE_SECRETA) y NO puede ser revertido.
💡 Importante:
- Los datos encriptados solo pueden ser verificados con la clave secreta.
- Si la clave no coincide, los datos no serán reconocidos por el sistema.
- Este método impide que la información sea alterada sin que lo notemos.



