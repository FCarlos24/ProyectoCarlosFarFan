import json
from estructuras import Pila, Cola, ListaDobleArchivos

class Archivo:
    def __init__(self, nombre, contenido=""):
        self.nombre = nombre
        self.contenido = contenido
        self.pila_undo = Pila()
        self.pila_redo = Pila()

    def modificar(self, nuevo_contenido):
        # Guardamos estado actual antes de cambiar
        self.pila_undo.apilar(self.contenido)
        self.pila_redo = Pila() # Se limpia el redo al hacer un cambio nuevo
        self.contenido = nuevo_contenido

    def undo(self):
        if not self.pila_undo.esta_vacia():
            self.pila_redo.apilar(self.contenido)
            self.contenido = self.pila_undo.desapilar()
            return True
        return False

    def redo(self):
        if not self.pila_redo.esta_vacia():
            self.pila_undo.apilar(self.contenido)
            self.contenido = self.pila_redo.desapilar()
            return True
        return False

class MiniIDE:
    def __init__(self):
        self.archivos = ListaDobleArchivos()
        self.activo = None
        self.cola_peticiones = Cola()
        self.config = {}
        
        # Datos por defecto para pruebas[cite: 3]
        archivo_prueba = Archivo("main.cpp", "int main() {\n  return 0;\n}")
        self.archivos.insertar(archivo_prueba)
        self.activo = archivo_prueba

    def cargar_config(self, ruta):
        try:
            with open(ruta, 'r') as f:
                self.config = json.load(f)
            return True
        except FileNotFoundError:
            return False
