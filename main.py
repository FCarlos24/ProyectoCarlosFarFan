from modelos import MiniIDE
from comandos import (CmdNew, CmdList, CmdSwitch, CmdDelete, CmdConfig, 
                      CmdCheck, CmdUndo, CmdRedo, CmdSort, CmdQueueStatus, 
                      CmdAnalyze, CmdWrite)

def principal():
    ide = MiniIDE()
    # Registro de comandos en el invocador
    comandos_disp = {
        "new": CmdNew(),
        "list": CmdList(),
        "switch": CmdSwitch(),
        "delete": CmdDelete(),
        "config": CmdConfig(),
        "check": CmdCheck(),
        "undo": CmdUndo(),
        "redo": CmdRedo(),
        "sort": CmdSort(),
        "queue-status": CmdQueueStatus(),
        "analyze": CmdAnalyze(),
        "write": CmdWrite() # Comando extra para poder insertar texto y probar undo/redo
    }

    print("Bienvenido al Proyecto de Carlos FarFan - CLI Mini IDE")
    print("Escribe tus comandos (Ej: list, new archivo.txt, write int x=0;)")

    while True:
        try:
            entrada = input("\n> ").strip().split()
            if not entrada:
                continue
            
            cmd = entrada[0].lower()
            args = entrada[1:]

            if cmd == "exit":
                print("Saliendo del IDE...")
                break
            
            if cmd in comandos_disp:
                comandos_disp[cmd].ejecutar(ide, args)
            else:
                print(f"Comando '{cmd}' no reconocido. (Menús deshabilitados por evaluación).")
        
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    principal()
