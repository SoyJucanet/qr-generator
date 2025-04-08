import qrcode
import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import qrcode.constants

contador_qr = 1
qr_image_tk = None
qr_preview_label = None

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def limpiar_entrada():
    entry.delete(0, tk.END)
    qr_preview_label.config(image="")

def generar_qr_desde_gui():
    global contador_qr, qr_image_tk

    enlace = entry.get().strip()
    if not enlace:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa un enlace.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(enlace)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    nombre_archivo = f"qr_jucanet_{contador_qr}.png"
    ruta_absoluta = os.path.join(os.getcwd(), nombre_archivo)
    img.save(ruta_absoluta)
    contador_qr += 1

    img_pil = Image.open(ruta_absoluta).resize((150, 150))
    qr_image_tk = ImageTk.PhotoImage(img_pil)
    qr_preview_label.config(image=qr_image_tk)

    messagebox.showinfo("¡Éxito!", f"Código QR generado y guardado en:\n{ruta_absoluta}")
    os.startfile(ruta_absoluta)

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Generador de QR's - Jucanet")
    ventana.configure(bg="#f2f2f2")
    ventana.resizable(False, False)
    centrar_ventana(ventana, 420, 500)

    contenedor = tk.Frame(ventana, bg="#f2f2f2")
    contenedor.pack(padx=20, pady=10)

    ttk.Separator(contenedor, orient='horizontal').pack(fill='x', pady=(5, 5))

    titulo = tk.Label(contenedor, text="GENERADOR DE QR'S", font=("Segoe UI", 16, "bold"), fg="red", bg="#f2f2f2")
    titulo.pack(pady=(5, 10))

    ttk.Separator(contenedor, orient='horizontal').pack(fill='x', pady=(0, 10))

    etiqueta = tk.Label(
        contenedor,
        text="Pega aquí el enlace que deseas convertir:",
        font=("Segoe UI", 11, "bold"),
        bg="#f2f2f2",
        anchor="w"
    )
    etiqueta.pack(fill="x", padx=10)

    entry = tk.Entry(contenedor, width=45, font=("Segoe UI", 10))
    entry.pack(pady=10)

    botones_frame = tk.Frame(contenedor, bg="#f2f2f2")
    botones_frame.pack()

    boton_generar = tk.Button(
        botones_frame,
        text="Generar QR",
        command=generar_qr_desde_gui,
        bg="#2E8B57",
        fg="white",
        activebackground="#246b45",
        font=("Segoe UI", 10, "bold"),
        width=12,
        relief="flat"
    )
    boton_generar.pack(side="left", padx=5)

    boton_limpiar = tk.Button(
        botones_frame,
        text="Limpiar",
        command=limpiar_entrada,
        bg="#cccccc",
        fg="black",
        activebackground="#b2b2b2",
        font=("Segoe UI", 10),
        width=8,
        relief="flat"
    )
    boton_limpiar.pack(side="left", padx=5)

    qr_preview_label = tk.Label(contenedor, bg="#f2f2f2")
    qr_preview_label.pack(pady=20)

    copyright = tk.Label(
        ventana,
        text="© Jucanet 2025",
        font=("Segoe UI", 9),
        bg="#f2f2f2",
        fg="gray"
    )
    copyright.pack(side="bottom", pady=10)

    try:
        ventana.mainloop()
    except Exception as e:
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(str(e))
        messagebox.showerror("Error", "Ha ocurrido un error. Revisa el archivo 'error_log.txt'.")
