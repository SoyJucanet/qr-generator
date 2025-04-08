📲 Jucanet QR Generator

Jucanet QR Generator es una aplicación de escritorio creada con Python que permite generar códigos QR a partir de enlaces de forma rápida y sencilla. Su interfaz gráfica amigable fue desarrollada con Tkinter.

🖼️ Captura de pantalla

🚀 Características

Interfaz gráfica intuitiva.

Generación de código QR a partir de un enlace.

Vista previa del QR generado.

El archivo se guarda automáticamente en la carpeta del programa.

Estilo visual personalizado (tipografías, colores, posición central, etc).

Ejecutable .exe disponible para Windows.

🛠️ Tecnologías utilizadas

Python 3

Tkinter

Pillow

qrcode

PyInstaller (para generar el .exe)

📆 Instalación desde código fuente

1. Clona el repositorio

git clone https://github.com/SoyJucanet/qr-generator.git
cd qr-generator

2. Instala las dependencias

pip install -r requirements.txt

Si no tienes el archivo requirements.txt, instala manualmente:

pip install qrcode[pil] pillow

3. Ejecuta la aplicación

python qrapp.py

💽 Versión ejecutable (Windows)

Si deseas ejecutar la aplicación directamente, puedes generar el .exe con:

pyinstaller --onefile --windowed --icon=logo.ico qrapp.py

El ejecutable se creará dentro de la carpeta dist/.

👨‍💻 Autor

Jucanet📧 jucanet.dev@gmail.com (reemplaza esto si quieres)💻 https://github.com/SoyJucanet

📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente. Consulta el archivo LICENSE para más información.
