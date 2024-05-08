from tkinter import *

class CenterWidgetMixin:
  
  #crearemos un metodo para que deje en el centro la ventana visual de tkinter
  def center(self):
    #actauliza la informacion con todos los elementos que hay dentro de la ventana
    self.update()
    #utilizamos la funcion geometry que es donde modificaremos
      #parametros para posicionar la ventana del tkinter
      
    #ancho ventana
    w = self.winfo_width()
    #alto ventana
    h = self.winfo_height()
    
    #ancho pantalla
    ws = self.winfo_screenwidth()
    
    hs = self.winfo_screenheight()
    
    #calculamos el posicionamiento de la ventana con respecto al tamano de la pantalla
    
    x = int(ws/2 - w/2)
    y = int(hs/2 - h/2)
    
    self.geometry(f"{w}x{h}+{x}+{y}")
  
class MainWindow(Tk, CenterWidgetMixin):
  def __init__(self):

      super().__init__()
      self.title("Gestor de clientes")  
      self.build()
      self.center()
  def build(self):
    button = Button(self, text="Hola", command=self.hola)
    button.pack()
  
  def hola(self):
    print("Hola mundo!")
  
  
    
if __name__ == "__main__":
  app = MainWindow()
  app.mainloop()