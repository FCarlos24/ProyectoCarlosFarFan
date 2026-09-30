from algoritmos import merge_sort, shellsort
from estructuras import Pila

class Comando:
    def ejecutar(self, ide, args):
        pass

class CmdNew(Comando):
    def ejecutar(self, ide, args):
        if not args:
            print("Falta el nombre del archivo. Uso: new <nombre>")
            return
        nombre = args[0]
        nuevo = ide.archivos.buscar(nombre)
        if nuevo:
            print(f"El archivo {nombre} ya existe.")
        else:
            from modelos import Archivo
            nuevo_archivo = Archivo(nombre)
            ide.archivos.insertar(nuevo_archivo)
            ide.activo = nuevo_archivo
            print(f"Archivo '{nombre}' creado y es ahora el activo.")

class CmdList(Comando):
    def ejecutar(self, ide, args):
        lista = ide.archivos.obtener_todos()
        if not lista:
            print("No hay archivos abiertos.")
            return
        print("Archivos abiertos:")
        for arch in lista:
            estado = "[ACTIVO]" if ide.activo and arch.nombre == ide.activo.nombre else ""
            print(f" - {arch.nombre} {estado}")

class CmdSwitch(Comando):
    def ejecutar(self, ide, args):
        if not args:
            print("Uso: switch <nombre>")
            return
        arch = ide.archivos.buscar(args[0])
        if arch:
            ide.activo = arch
            print(f"Cambiaste a '{arch.nombre}'.")
        else:
            print("Archivo no encontrado.")

class CmdDelete(Comando):
    def ejecutar(self, ide, args):
        if not args:
            print("Uso: delete <nombre>")
            return
        nombre = args[0]
        exito = ide.archivos.eliminar(nombre)
        if exito:
            if ide.activo and ide.activo.nombre == nombre:
                ide.activo = None
            print(f"Archivo '{nombre}' eliminado de memoria.")
        else:
            print("Archivo no encontrado.")

class CmdConfig(Comando):
    def ejecutar(self, ide, args):
        if not args:
            print("Uso: config <ruta>")
            return
        if ide.cargar_config(args[0]):
            print(f"Configuración cargada desde '{args[0]}'.")
        else:
            print("Error al leer archivo de configuración.")

class CmdCheck(Comando):
    def ejecutar(self, ide, args):
        if not ide.activo:
            print("No hay archivo activo.")
            return
        pila = Pila()
        lineas = ide.activo.contenido.split('\n')
        pares = {')': '(', '}': '{', ']': '['}
        
        for i, linea in enumerate(lineas):
            for j, char in enumerate(linea):
                if char in "({[":
                    pila.apilar((char, i + 1, j + 1))
                elif char in ")}]":
                    if pila.esta_vacia():
                        print(f"Error de sintaxis: '{char}' de cierre sin apertura en línea {i+1}, pos {j+1}.")
                        return
                    cima, l, c = pila.desapilar()
                    if cima != pares[char]:
                        print(f"Error de sintaxis: Se esperaba cierre para '{cima}', pero se encontró '{char}' en línea {i+1}.")
                        return
        
        if not pila.esta_vacia():
            cima, l, c = pila.desapilar()
            print(f"Error: '{cima}' abierto en línea {l} nunca se cerró.")
        else:
            print("Validación completada: Símbolos de agrupación balanceados.")

class CmdUndo(Comando):
    def ejecutar(self, ide, args):
        if ide.activo and ide.activo.undo():
            print("Cambio deshecho (Undo).")
        else:
            print("No hay cambios para deshacer o no hay archivo activo.")

class CmdRedo(Comando):
    def ejecutar(self, ide, args):
        if ide.activo and ide.activo.redo():
            print("Cambio rehecho (Redo).")
        else:
            print("No hay cambios para rehacer.")

class CmdSort(Comando):
    def ejecutar(self, ide, args):
        if len(args) < 2:
            print("Uso: sort <criterio(linea/gravedad)> <algoritmo(mergesort/shellsort)>")
            return
        criterio, algoritmo = args[0], args[1]
        if criterio not in ['linea', 'gravedad']:
            print("Criterio inválido.")
            return
            
        # Alertas dummy para procesar el motor de ordenamiento
        diagnosticos = [
            {"linea": 45, "gravedad": 3, "msj": "Complejidad ciclomática alta"},
            {"linea": 12, "gravedad": 1, "msj": "Variable sin uso"},
            {"linea": 30, "gravedad": 2, "msj": "Falta validación"}
        ]
        
        if algoritmo == "mergesort":
            res = merge_sort(diagnosticos, criterio)
        elif algoritmo == "shellsort":
            res = shellsort(diagnosticos, criterio)
        else:
            print("Algoritmo no soportado.")
            return
            
        print(f"Resultados ordenados por {criterio}:")
        for d in res:
            print(f"Línea: {d['linea']}, Gravedad: {d['gravedad']} -> {d['msj']}")

class CmdQueueStatus(Comando):
    def ejecutar(self, ide, args):
        print(f"Peticiones en cola hacia la API: {ide.cola_peticiones.tamano}")

class CmdAnalyze(Comando):
    def ejecutar(self, ide, args):
        if not ide.activo:
            print("No hay archivo activo.")
            return
        ide.cola_peticiones.encolar({"archivo": ide.activo.nombre, "tipo": "analisis"})
        print(f"Análisis encolado para {ide.activo.nombre}.")

# Comando extra agregado estrictamente para probar el Undo/Redo modificando el texto.
class CmdWrite(Comando):
    def ejecutar(self, ide, args):
        if not ide.activo:
            print("No hay archivo activo.")
            return
        texto = " ".join(args)
        ide.activo.modificar(texto)
        print(f"Texto escrito en {ide.activo.nombre}.")
