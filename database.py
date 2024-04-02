#este archivo aportara los datos como tal
  #y proveera una interfaz para crear modificar eliminar informacion
  
  
#importamos el modulo de csv
import csv

#importamos constantes establecidas en un script alternos

import config
  #creamos clase para manejar un cliente
  
class Cliente:
  
  #al constructor inicial le asignamos unas propiedades que tendra nuestra clase
    #las cuales recibira los datos atraves del parametro
  
  def __init__(self, dni, nombre, apellido):
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    
  #establecemos funcion string para devolver el cliente
  
  def __str__(self):
    return f"({self.dni} {self.nombre}  {self.apellido})"
  
  

#crearemos ahora el sistema que manejara los clientes
  #creamos una clase Clientes plural
class Clientes:
  
  #manejaremos mentodo estaticos y no utilizando instancia
    #por eso establecemos una lista en el nievel principal de la clase 
  lista = []

  #parte del ejemplo csv
  
  #abrimos el fichero y le asignamos un alias
  with open(config.DATABASE_PATH, newline='\n') as fichero:
    #utilizamos el modulo csv para poder interactuar con el fichero
      #utilizamos el metodo reader que recibe el fichero y el delimitador
        #quen es la forma en la que separamos los datos dentro del fichero
    reader = csv.reader(fichero, delimiter=';')
    #luego recorremos cada linea del fichero y podemos extraer cada uno
      #de los datos separados por ; en una variable
    for dni, nombre, apellido in reader:
      #con estos datos creamos un cliente apartir de una instancia
      cliente = Cliente(dni,nombre, apellido)
      
      #anadimos los datos ya recorridos de el csv a la lista de clientes 
      lista.append(cliente)
      
  
  #definimos un metodo estatico con un decorador 
  
  #con este metodo buscaremos un cliente  
    #recorriendo la lista que establecimos al inicio y luego
      # comparar el dni buscado con el dni que recorremos de la lista
  @staticmethod
  def buscar(dni):
    for cliente in Clientes.lista:
      if cliente.dni == dni:
        return cliente
      
      
  @staticmethod
  def crear(dni, nombre, apellido):
    #creamos una instancia de la clase Cliente
    cliente = Cliente(dni, nombre, apellido)
    #luego anadimos el cliente que generamos de la instancia a nuestra lista
      #de clientes que generamos 
    Clientes.lista.append(cliente)
    Clientes.guardar()
    return cliente
  
  
  @staticmethod
  def modificar(dni, nombre, apellido):
    #recorremos el cliente pero esta vez solicitamos el indice
      #para saber la posicion en la lista del cliente que queremos modificar
    for indice, cliente in enumerate(Clientes.lista):
      #que coincida el dni del cliente que queremos cambiar 
      if cliente.dni == dni:
        #luego cambiaremos el campo especificamente por lo nuevo que estamos
          #pasando por parametro en el metodo modificar
        Clientes.lista[indice].nombre = nombre
        Clientes.lista[indice].apellido = apellido
        Clientes.guardar()
        return Clientes.lista[indice]
  
  @staticmethod
  def borrar(dni):
    for indice, cliente in enumerate(Clientes.lista):
      if cliente.dni == dni:
        cliente = Clientes.lista.pop(indice)
        Clientes.guardar()
        return cliente
      
#funcion implementada para pasar los cambios generados
  #en los datos de los clientes para pasarlos
    #a el archivo csv todos los datos en general 
    
  @staticmethod
  def guardar():
    #abrimos el archivo csv en modo escritura
    with open(config.DATABASE_PATH, 'w', newline="\n") as fichero:
      #lemos el fichero y delimitamos sus datos
      writer = csv.writer(fichero, delimiter=";")
      #luego de eso recorremos la lista de los clientes 
        #en la cual por cada cliente en cada linea del archivo
          #agregaremos sus datos completos 
      for cliente in Clientes.lista:
        writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
        
      