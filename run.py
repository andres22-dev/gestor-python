import ui
import sys

#en este script sera el que ejecutara toda la aplicacion

#importamos el menu
import menu 

#comprobamos que se esta ejecutando desde el principal
if __name__ == "__main__":
  #del modulo menu ejecutamos la funcion iniciar 
  
  if len(sys.argv) > 1 and sys.argv[1] == "-t":
    menu.iniciar()
  else:
    app = ui.MainWindow()
    app.mainloop()