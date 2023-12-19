

from NodoEntrada import *
class ListaEnlazadaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def agregar_inicio(self, dato):
        nuevo_nodo = nodoEntrada(dato)

        if self.esta_vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo

    def agregar_final(self, dato):
        nuevo_nodo = nodoEntrada(dato)

        if self.esta_vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    
    def obtener_primero(self):
        if not self.esta_vacia():
            return self.primero.dato
        else:
            return None

    def obtener_siguiente(self):
        if self.primero is None or self.primero.siguiente is None:
            return None, None, None  

        try:
            siguiente_nodo = self.primero.siguiente
            siguiente_dato = siguiente_nodo.dato
            siguiente_ruta = siguiente_dato.ruta
            siguiente_imagen = siguiente_dato.imagen
            
            self.primero = siguiente_nodo

            return siguiente_dato, siguiente_ruta, siguiente_imagen
        except AttributeError as e:
            print(f"Error al obtener datos del nodo siguiente: {e}")
            return None, None, None



        
    def obtener_anterior(self):
        if self.primero is None or self.primero.anterior is None:
            return None, None, None 

        try:
            anterior_nodo = self.primero.anterior
            anterior_dato = anterior_nodo.dato
            anterior_ruta = anterior_dato.ruta
            anterior_imagen = anterior_dato.imagen
            
            self.primero = anterior_nodo

            return anterior_dato, anterior_ruta, anterior_imagen
        except AttributeError as e:
            print(f"Error al obtener datos del nodo anterior: {e}")
            return None, None, None  
