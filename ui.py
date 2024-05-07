from tkinter import *

#heredamos de tk en vez de utilizar root 
  #entonces mainwindow se convertira en la parte que gestionara
    #la parte principal de la interfaz
class MainWindow(Tk):
  #definimos el constructor
  def __init__(self):
    #utilizamos la funcion super para llamar de la superclase que estamos
      #heredando ue es tk el metodo init que tiene internamente 
      super().__init__()
      #haciendo referencia a la intancia de la ventana podremos 
        #ya mismo realizar modificaciones sobre ella
      self.title("Gestor de clientes")
      
  #separamos la construccion de la venta en otro metodo 
  
  def build(self):
    button = Button(self, text="Hola", command=self.hola)
    button.pack()
  
  def hola(self):
    print("Hola mundo!")
    
if __name__ == "__main":
  app = MainWindow()
  app.mainloop()