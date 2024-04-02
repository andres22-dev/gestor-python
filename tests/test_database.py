#importamos la libreria que nos permitira hacer las pruebas
import sys
sys.path.append('..')
import config
import csv 
import copy 
import unittest
import helpers

#importamos el script donde establecimos la base de datos
  #al cual le pondremos un alias para abreviarlo
import database as db 

class TestDatabase(unittest.TestCase):
  
  def setUp(self):
    
    #utilizando la importacion de la db hacemos uso de las clases de este
      # accediendo a la lista donde guardamos los clientes y a la 
        #clase que nos permite crear un cliente 
    db.Clientes.lista = [
      db.Cliente('15J', 'Marta', 'Perez'),
      db.Cliente('48H', 'Manolo', 'Lopez'),
      db.Cliente('28Z', 'Ana', 'Garcia'),
      ]
    
  def test_buscar_cliente(self):
    cliente_existente = db.Clientes.buscar('15J')
    cliente_inexistente = db.Clientes.buscar('99X')
    
    #hacemos la comprobacion de lo que devuelve el uso del dni que estamos buscando
      #como prueba 
    self.assertIsNotNone(cliente_existente)
    self.assertIsNone(cliente_inexistente)
    
  def test_crear_cliente(self):
    nuevo_cliente = db.Clientes.crear('39X', 'Hector', 'Costa')
    #verificando que el cliente esta creando comparando la longitud de la lista
      #si esta pues es mas grande significaria queel cliente quedo creado
    self.assertEqual(len(db.Clientes.lista), 4)
    self.assertEqual(nuevo_cliente.dni, '39X')
    self.assertEqual(nuevo_cliente.nombre, 'Hector')
    self.assertEqual(nuevo_cliente.apellido, 'Costa')
    
    
  def test_modificar_cliente(self):
    cliente_a_modificar = copy.copy(db.Clientes.buscar('28Z'))
    cliente_modificado = db.Clientes.modificar('28Z', 'Mariana', 'Garcia')
    self.assertEqual(cliente_a_modificar.nombre, 'Ana')
    self.assertEqual(cliente_modificado.nombre, 'Mariana')
    
  
  def test_borrador_cliente(self):
    #aqui sacamos el cliente de la lista y lo almacenamos en una variable
    cliente_borrado = db.Clientes.borrar('48H')
    
    #comprobamos que ese dato esta pero como ese 
      #dato ya fue borrado devolveria none
    cliente_rebuscado = db.Clientes.buscar('48H')
    self.assertEqual(cliente_borrado.dni, '48H')
    self.assertIsNone(cliente_rebuscado)
    
  def test_dni_valido(self):
    self.assertTrue(helpers.dni_valido('00A',db.Clientes.lista))
    self.assertFalse(helpers.dni_valido('372837', db.Clientes.lista))
    self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
    self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))
    
  def test_escritura_csv(self):
    db.Clientes.borrar('48H')
    db.Clientes.borrar('15J')
    db.Clientes.modificar('28Z', 'Mariana', 'Garcia')
    
    
    dni, nombre, apellido = None, None, None
    
    with open(config.DATABASE_PATH,newline="\n") as fichero:
      reader = csv.reader(fichero, delimiter=";")
      dni, nombre, apellido = next(reader)
      
    self.assertEqual(dni, '28Z')
    self.assertEqual(nombre, 'Mariana')
    self.assertEqual(apellido, 'Garcia')