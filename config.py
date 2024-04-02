#este archivo contendra constantes de configuracion
import sys 

DATABASE_PATH = "clientes.csv"

#si al momento de ejecutar el archivo se encuentras
  #el argumento en la lista de argumentos que se almacenan 
    #en una lista al correr el script es pytest 

if "pytest" in sys.argv[0]:
  
  #entonces que corrija la ruta que se esta ejecutando
    #por una que sea propiamente para testeos 
  DATABASE_PATH = "tests/clientes_test.csv"