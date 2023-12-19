import xml.etree.ElementTree as ET
from ListaDoble import *
from DatosCancion import cancion

lista_cancion = ListaEnlazadaDoble()

def carga(archivo):
    contenido_interfaz = ""
    
    try:
        tree = ET.parse(archivo)
        raiz = tree.getroot()

        lista_externa_temp = ListaEnlazadaDoble()

        for ext_temp in raiz.findall('cancion'):
            artista_cancion = ext_temp.find('artista').text
            album_cancion = ext_temp.find('album').text
            imagen_cancion = ext_temp.find('imagen').text
            ruta_cancion = ext_temp.find('ruta').text

            datos = cancion(artista_cancion, album_cancion, imagen_cancion, ruta_cancion)
            lista_externa_temp.agregar_inicio(datos)

            contenido_interfaz += f"-Artista: {artista_cancion},\n -Album: {album_cancion},\n -Ruta de Imagen: {imagen_cancion},\n -Ruta de archivo: {ruta_cancion}\n"

        print("Carga exitosa ")
        return lista_externa_temp, contenido_interfaz

    except FileNotFoundError:
        print("El documento no existe o se escribió de manera incorrecta")
        return None, ""

    except ET.ParseError as e:
        print("Error al analizar el archivo XML:", e)
        return None, ""



def html(nombre_archivo):

        lista_canciones = ListaEnlazadaDoble()
        lista_canciones.agregar_inicio(cancion(artista="Artista1", album="Album1", imagen="imagen1", ruta="ruta1"))
        lista_canciones.agregar_inicio(cancion(artista="Artista2", album="Album2", imagen="imagen2", ruta="ruta2"))
        lista_canciones.agregar_inicio(cancion(artista="Artista3", album="Album3", imagen="imagen3", ruta="ruta3"))

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

            auxiliar = lista_canciones.primero
            while auxiliar is not None:
                archivo.write('<tr>\n')
                archivo.write(f'<td>{auxiliar.dato.artista}</td>\n')
                archivo.write(f'<td>{auxiliar.dato.album}</td>\n')
                archivo.write(f'<td>{auxiliar.dato.imagen}</td>\n')
                archivo.write(f'<td>{auxiliar.dato.ruta}</td>\n')
                archivo.write('</tr>\n')
                auxiliar = auxiliar.siguiente

            archivo.write('</table>\n')
            archivo.write('</body>\n')
            archivo.write('</html>\n')