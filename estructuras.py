class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nuevo = NodoSimple(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def desapilar(self):
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def esta_vacia(self):
        return self.tope is None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0

    def encolar(self, dato):
        nuevo = NodoSimple(dato)
        if self.esta_vacia():
            self.frente = nuevo
        else:
            self.final.siguiente = nuevo
        self.final = nuevo
        self.tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamano -= 1
        return dato

    def esta_vacia(self):
        return self.frente is None

class ListaDobleArchivos:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, archivo):
        nuevo = NodoDoble(archivo)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def buscar(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.dato.nombre == nombre:
                return actual.dato
            actual = actual.siguiente
        return None

    def eliminar(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.dato.nombre == nombre:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def obtener_todos(self):
        archivos = []
        actual = self.cabeza
        while actual:
            archivos.append(actual.dato)
            actual = actual.siguiente
        return archivos
