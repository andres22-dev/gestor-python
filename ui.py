import database as db
from tkinter import *
from tkinter import ttk
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
    #vamos a mostrar en forma de tabla la informacion de los clientes con un frame 
    frame = Frame(self)
    frame.pack()
    
    treeview = ttk.Treeview(frame)
    
    #configuracion de columnas 
    treeview['columns'] = ('DNI', 'Nombre', 'Apellido')
    
    #borramos la primera columna que se genera por defecto
    treeview.column('#0', width=0, stretch=NO)
    
    #personalizamos las otras columnas
    
    treeview.column('DNI',  anchor=CENTER)
    treeview.column('Nombre',  anchor=CENTER)
    treeview.column('Apellido',  anchor=CENTER)
  
    #configuracion de las cabezeras o nonbres en la tabla 
    
    treeview.heading("DNI", text="DNI", anchor=CENTER)
    treeview.heading("Nombre", text="Nombre", anchor=CENTER)
    treeview.heading("Apellido", text="Apellido", anchor=CENTER)
    
    
    #creamos un scroll por si la tabla es muy grande y necesitamos desplazarnos en la ventana
    
    scrollbar = Scrollbar(frame)
    #establecemos la posicion del scrool y el eje x o y
    scrollbar.pack(side=RIGHT, fill=Y)
    treeview['yscrollcommand'] = scrollbar.set
    
    #importamos la base de datos y recorremos los registros

    for cliente in db.Clientes.lista:
      #insertamos los datos dentro de la tabla para
      treeview.insert(
        parent='',index='end',iid=cliente.dni,
        values=(cliente.dni, cliente.nombre, cliente.apellido))
      
    
    treeview.pack()
    
    
    frame = Frame(self)
    frame.pack(pady=20)
    Button(frame, text="Crear", command=None).grid(row=0, column=0)
    Button(frame, text="Modificar", command=None).grid(row=0, column=1)
    Button(frame, text="Borrar", command=None).grid(row=0, column=2)

    
if __name__ == "__main__":
  app = MainWindow()
  app.mainloop()