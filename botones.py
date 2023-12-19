import tkinter as tk

class BotonImagen:
    def __init__(self, ventana, normal_img, activa_img, command, x, y):
        self.normal_img = tk.PhotoImage(file=normal_img)
        self.activa_img = tk.PhotoImage(file=activa_img)

        self.boton = tk.Button(ventana, command=command, image=self.normal_img)
        self.boton.place(x=x, y=y)

        self.boton.bind("<Enter>", self.cambiar_imagen_activa)
        self.boton.bind("<Leave>", self.restaurar_imagen)

    def cambiar_imagen_activa(self, event):
        self.boton.config(image=self.activa_img)

    def restaurar_imagen(self, event):
        self.boton.config(image=self.normal_img)

