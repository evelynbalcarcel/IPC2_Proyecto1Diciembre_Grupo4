from tkinter import *
from tkinter import messagebox
from NodoEntrada import nodoEntrada
from ListaDoble import ListaEnlazadaDoble
from DatosCancion import *

class reporte:
    def html(nombre_archivo,listado):

        with open(nombre_archivo, 'w') as archivo:
            archivo.write('<!DOCTYPE html>\n')
            archivo.write('<html>\n')
            archivo.write('<head>\n')
            archivo.write('<title>Reporte de canciones mas escuchadas</title>\n')
            archivo.write('<style>\n')
            archivo.write('body {background-color: #000123; color: #000123;} /* Fondo negro y letras negras */\n')
            archivo.write('table {border-collapse: collapse; width: 80%; margin: 20px auto;}\n')
            archivo.write('th, td {border: 1px solid black; padding: 8px; text-align: left;}\n')
            archivo.write('tr:nth-child(even) {background-color: #f0f8ff;}\n')  # Celeste (Blue)
            archivo.write('tr:nth-child(odd) {background-color: #f1bbbb;}\n')  # Celeste más pálido (Silver)
            archivo.write('h1 {text-align: center; color: #fff;} /* Título en blanco */\n')
            archivo.write('</style>\n')
            archivo.write('</head>\n')
            archivo.write('<body>\n')
            archivo.write('<h1>Reporte de canciones mas escuchadas</h1>\n')
            archivo.write('<table>\n')
            archivo.write('<tr>\n')
            archivo.write('<th>Artista</th>\n')
            archivo.write('<th>Album</th>\n')
            archivo.write('<th>Imagen</th>\n')
            archivo.write('<th>Ruta</th>\n')
            archivo.write('</tr>\n')

            auxiliar = listado.primero
            while auxiliar is not None:
                archivo.write('<tr>\n')
                archivo.write(f'<td>{auxiliar.dato.artista}</td>\n')
                archivo.write(f'<td>{auxiliar.dato.album}</td>\n')
                archivo.write(f'<td><a href="{auxiliar.dato.ruta}">Reproducir</a></td>\n')
                archivo.write(f'<td><img src="{auxiliar.dato.imagen}" width="100" height="100"></td>\n')
                archivo.write('</tr>\n')
                auxiliar = auxiliar.siguiente

            archivo.write('</table>\n')
            archivo.write('</body>\n')
            archivo.write('</html>\n')




