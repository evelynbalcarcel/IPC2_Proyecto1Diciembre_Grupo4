import tkinter as tk
from tkinter import ( filedialog,  ttk,scrolledtext)
from botones import  *
import pygame
from graphviz import Digraph
from reporteHTML import *
from PIL import ImageTk, Image
#-------

import lecturaXml


#reporte html
def generar_reporte_html():
    reporte.html('reporte_HTML.html',lista_externa_temp)
    messagebox.showinfo("Generar Reporte", "Reporte de html generado.")


def generar_grafico_lista(lista):
    dot = Digraph(comment='Lista Enlazada Doble', format='png')

    # Configuración de nodos y bordes
    dot.node('Inicio', label='Inicio', shape='circle')
    dot.node('Fin', label='Fin', shape='circle')

    # Recorrido de la lista para agregar nodos y enlaces
    nodo_actual = lista.primero
    while nodo_actual is not None:
        nodo_id = f'Nodo_{nodo_actual.dato.artista}_{nodo_actual.dato.album}'
        dot.node(nodo_id, label=f'{nodo_actual.dato.artista}\n{nodo_actual.dato.album}', shape='box', style='filled', fillcolor='#f0f8ff', fontcolor='#000')
        dot.edge('Inicio', nodo_id) if nodo_actual.anterior is None else dot.edge(f'Nodo_{nodo_actual.anterior.dato.artista}_{nodo_actual.anterior.dato.album}', nodo_id)
        nodo_actual = nodo_actual.siguiente

    dot.edge(f'Nodo_{lista.ultimo.dato.artista}_{lista.ultimo.dato.album}', 'Fin') if lista.ultimo is not None else None

    # Guardar el gráfico como imagen
    dot.render('lista_grafico', format='png', cleanup=True)


    generar_grafico_lista(lista_externa_temp)


#funciones 
#combobox
def seleccionar_opcion(event):
    opcion_seleccionada = combo.get()
    
    if opcion_seleccionada == "Salir":
        ventana.destroy()

    if opcion_seleccionada == "Abrir":
        abrir_archivo()
        
    elif opcion_seleccionada == "Reporte Html":
        print("Se ha solicitado el reporte ")
        generar_reporte_html()


    elif opcion_seleccionada == "Reporte Grafico":
        print("Se ha solicitado el reporte ")
        generar_grafico_lista(lista_externa_temp)



def abrir_archivo():
    global lista_externa_temp, ruta_cancion, ruta_imagen

    archivo = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.xml"), ("Todos los archivos", "*.xml*")])
    if archivo:

        lista_externa_temp, contenido_interfaz = lecturaXml.carga(archivo)
        ruta_imagen, ruta_cancion = obtener_primero()

    cuadro_texto.delete('1.0', tk.END)
    cuadro_texto.insert(tk.END, contenido_interfaz)

    abrir_imagen(ruta_imagen)
    play_musica(ruta_cancion)
    
    return lista_externa_temp


def obtener_primero():
    global lista_externa_temp, ruta_cancion, ruta_imagen

    primer_elemento = lista_externa_temp.obtener_primero()
    if primer_elemento is not None:
        ruta_cancion = primer_elemento.ruta
        ruta_imagen = primer_elemento.imagen
        return ruta_imagen, ruta_cancion

def abrir_imagen(imagen_primaria):

    global imagen_actual
    imagen_actual = imagen_primaria
    if imagen_actual:  # Verifica si la ruta de la imagen está definida (obtenida previamente)
        imagen = Image.open(imagen_actual)
        imagen = imagen.resize((300, 300))
        imagen_actual = ImageTk.PhotoImage(imagen)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=imagen_actual)
        print(imagen_actual)
    else:
        print("La ruta de la imagen no está definida")  # Mensaje de error si la ruta no está definida


def mostrar_siguiente():
    global lista_externa_temp

    siguiente_elemento, siguiente_ruta, siguiente_imagen = lista_externa_temp.obtener_siguiente()
    if siguiente_elemento is not None:
        abrir_imagen(siguiente_imagen)
        play_musica(siguiente_ruta)

        print("Siguiente elemento:", siguiente_elemento)
        print("Ruta de la imagen:", siguiente_imagen)
        print("Ruta de la cancion: ", siguiente_ruta)
    else:
        print("No hay siguiente elemento")

def mostrar_anterior():
    global lista_externa_temp

    anterior_elemento, anterior_ruta, anterior_imagen = lista_externa_temp.obtener_anterior()
    if anterior_elemento is not None:
        abrir_imagen(anterior_imagen)
        play_musica(anterior_ruta)

        print("Elemento anterior:", anterior_elemento)
        print("Ruta de la imagen:", anterior_imagen)
        print("Ruta de la canción:", anterior_ruta)
    else:
        print("No hay elemento anterior")
#botones de la musica
playing = False

def play_musica(ruta_musica):
    global playing

    print(ruta_musica)
    
    if not playing:
        pygame.mixer.music.load(ruta_musica)
        pygame.mixer.music.play()
        pygame.time.wait(100)  # Espera un poco después de cargar la música
        playing = True
    else:
        if pygame.mixer.music.get_busy():  # Verifica si hay música reproduciéndose
            pygame.mixer.music.pause()
            playing = False
        else:
            pygame.mixer.music.unpause()
            playing = True

def pause_musica():
    global playing
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        playing = True

def stop_musica():
    global playing
    pygame.mixer.music.stop()
    playing = False




#interfaz
ventana = tk.Tk()
ventana.title("Reproductor de musica")
ventana.geometry("800x650") 
ventana.configure(bg="#2F2B2B")


combo = ttk.Combobox(ventana, width=15, height=25, values=("Abrir", "Reporte Html", "Reporte Grafico", "Salir"),
                    state='readonly', font=("Comic Sans Ms", 15))
combo.set("Archivo")  
combo.place(x=50,y=50)
combo.bind("<<ComboboxSelected>>", seleccionar_opcion)


#frame para el cuadro de texto
frame_cuadro_texto = tk.Frame(ventana)
frame_cuadro_texto.configure(highlightbackground="#131A3E")
frame_cuadro_texto.place(x=375,y=200)
#cuadro editable 
cuadro_texto = scrolledtext.ScrolledText(frame_cuadro_texto, wrap=tk.WORD, width=40, height=15)
cuadro_texto.pack(expand=True, fill='both')
cuadro_texto.configure(highlightbackground="#131A3D")


#imagen predeterminada 
imagen_predeterminada = Image.open("imagenes/imagenPredeterminada.jpg")
imagen_predeterminada = imagen_predeterminada.resize((300, 300))
i_predeterminada = ImageTk.PhotoImage(imagen_predeterminada)

#canva de la imagen
canvas = tk.Canvas(ventana, width=300, height=300)
canvas.place(x=50,y=200)
canvas.create_image(0,0, anchor= "nw", image = i_predeterminada)



#botones de abajo
boton_izquierda = BotonImagen(ventana, "imagenes/izquierda1.png","imagenes/izquierda2.png",mostrar_anterior, 375, 450)
boton_derecha = BotonImagen(ventana, "imagenes/derecha1.png","imagenes/derecha2.png",mostrar_siguiente, 590, 450)

#arriba
boton_play = BotonImagen(ventana, "imagenes/play.png", "imagenes/play2.png", lambda: play_musica(ruta_cancion), 515, 130)
boton_pause = BotonImagen(ventana,"imagenes/pausa.png","imagenes/pausa2.png",pause_musica, 415, 130)
boton_stop = BotonImagen(ventana, "imagenes/stop.png","imagenes/stop2.png",stop_musica, 615, 130)


pygame.mixer.init()
ventana.mainloop()