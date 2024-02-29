#importamos la libreria que nos permitira hacer las pruebas

import unittest

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