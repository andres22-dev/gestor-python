#el que unira el script principal a traves del menu
  #interactuaremos con la base de datos 
import os  
def iniciar():
  while True:
    #borramos lo que estemos ejecutando continuamente en terminal
    os.system('clear')
    print("================")
    print(" Bienvenido al Gestor")
    print("================")
    print("[1] Listar los clientes ")
    print("[2] Buscar un cliente ")
    print("[3] Anadir un cliente")
    print("[4] Modificar un cliente")
    print("[5] Borrar un cliente")
    print("[6] Cerrar el Gestor")
    print("================")
    
    opcion = input(">")
    os.system('clear')
    
    if opcion == '1':
      print("Listando los clientes...\n")
      #todo
    elif opcion == '2':
      print("Buscando un cliente...\n")
      #todo
    elif opcion == '3':
      print("Anadiendo un cliente...\n")
      #todo
    elif opcion == '4':
      print("Modificando un cliente...\n")
      #todo
    elif opcion == '5':
      print("Borrando un cliente...\n")
      #todo
    elif opcion == '6':
      print("Saliendo")
      break
    
  input("\n Presiona ENTER para continuar..")