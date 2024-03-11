#el que unira el script principal a traves del menu
  #interactuaremos con la base de datos 
import os 
import helpers
import database as db
def iniciar():
  while True:
    #borramos lo que estemos ejecutando continuamente en terminal
    helpers.limpiar_pantalla()
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
    helpers.limpiar_pantalla
    
    if opcion == '1':
      print("Listando los clientes...\n")
      for cliente in db.Clientes.lista:
        print(cliente)
        
    elif opcion == '2':
      print("Buscando un cliente...\n")
      #ingresamos por pantalla un dni con la 
        #funcion auxiliar y trasnformamos el text a mayus
      dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
      cliente = db.Clientes.buscar(dni)
      #si el cliente no existe se mostrara un mensaje
      print(cliente) if cliente else print("Cliente no encontrado")
      
    elif opcion == '3':
      print("Anadiendo un cliente...\n")
      #leemos primero el dni
      dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
      nombre = helpers.leer_texto(2, 30, "NOMBRE (de 2 a 30 char)").capitalize()
      apellido = helpers.leer_texto(2, 30, "NOMBRE (de 2 a 30 char)").capitalize()
      db.Clientes.crear(dni, nombre, apellido)
      print("Cliente anadido correctamente ")
      
    elif opcion == '4':
      print("Modificando un cliente...\n")
      #leemos el dni en pantalla
      dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
      #buscamos si existe el cliente
      cliente = db.Clientes.buscar(dni)
      
      #si existe lo modificamos el nombre y el apellido 
      if cliente:
        #capturamos los nuevos datos a modificar en una variable 
        nombre = helpers.leer_texto(2, 30, f"NOMBRE (de 2 a 30 char) [{cliente.nombre}]").capitalize()
        apellido = helpers.leer_texto(2, 30, f"NOMBRE (de 2 a 30 char) [{cliente.apellido}]").capitalize()

        db.Clientes.modificar(cliente.dni, nombre, apellido)
        print("CLiente modificado correctamente")
      
      else:
        print("Clienet no encontrado")
      
    elif opcion == '5':
      print("Borrando un cliente...\n")
      #todo
    elif opcion == '6':
      print("Saliendo")
      break
    
  input("\n Presiona ENTER para continuar..")