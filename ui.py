import database as db
import helpers
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING
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

#creamos una clase nueva para desarrollar el popup para la crud
  #heredamos de dos clases toplevel y centerwidget
    #TopLevel es un widget que se encargara de manejar las subventanas
    #El mizin lo utilizaremos para centrar las ventanas 

class CreateClientWindow(Toplevel, CenterWidgetMixin):
  #definimos el constructor
  def __init__(self, parent):
    super().__init__(parent)
    self.title("crear cliente ")
    self.build()
    self.center()
  
  
  #obligamos al usuario a interactuar con la ventana 
    #antes de ir hacia la ventana principal
        
    self.transient(parent)
    self.grab_set()
      
      
  #disenos de la ventana   
  def build(self):
    frame = Frame(self)
    frame.pack(padx=20, pady=10)
    
    Label(frame, text="DNI (2 ints y 1 upper char)").grid(row=0, column=0)
    Label(frame, text="Nombre (de 2 a 30 chars)").grid(row=0, column=1)
    Label(frame, text="Apellido (de 2 a 30 chars)").grid(row=0, column=2)
    
    #campos de texto
    dni = Entry(frame)
    dni.grid(row=1, column=0)
    dni.bind("<KeyRelease>", lambda event: self.validate(event,0))
    
    nombre = Entry(frame)
    nombre.grid(row=1, column=1)
    nombre.bind("<KeyRelease>", lambda event: self.validate(event, 1))
    
    apellido = Entry(frame)
    apellido.grid(row=1, column=2)
    apellido.bind("<KeyRelease>", lambda event: self.validate(event,2))
    
    
    #crearemos otro frame 
    
    frame = Frame(self)
    frame.pack(pady=10)
    
    #boton para generar creacion cliente
    crear = Button(frame, text="Crear", command=self.create_client)
    crear.configure(state=DISABLED)
    crear.grid(row=0, column=0)
    Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)
    
    
    self.validaciones = [0, 0, 0]
    self.crear = crear
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    
  def create_client(self):
    self.master.treeview.insert(
        parent='',index='end',iid=self.dni.get(),
        values=(self.dni.get(), self.nombre.get(), self.apellido.get()))
    self.close()
  
  def close(self):
    self.destroy()
    self.update()
    
  #definimos nuestra funcion para validar los datos
  
  def validate(self, event, index):
    
    #traemos el valor del widget en el que se encuentra
    
    valor = event.widget.get()
    if index == 0:
      valido = helpers.dni_valido(valor, db.Clientes.lista)
      if valido:
        #si es valido pintamos de verde el campo
        event.widget.configure({"bg":"Green"})
        self.validaciones[index] = valido
      else:
        event.widget.configure({"bg":"Red"})
    if index == 1:
      valido = valor.isalpha() and len(valor) >= 2 and len(valor) <=30
      if valido:
        #si es valido pintamos de verde el campo
        event.widget.configure({"bg":"Green"})
        self.validaciones[index] = valido
      else:
        event.widget.configure({"bg":"Red"})
    if index == 2:
      valido = valor.isalpha() and len(valor) >= 2 and len(valor) <=30
      if valido:
        #si es valido pintamos de verde el campo
        event.widget.configure({"bg":"Green"})
        self.validaciones[index] = valido
      else:
        event.widget.configure({"bg":"Red"})
        
      #Cambiaremos el estado del boton con base a las validaciones 
      self.crear.config(state=NORMAL if self.validaciones == [1,1,1] else DISABLED)
      
        
class EditClientWindow(Toplevel, CenterWidgetMixin):
  def __init__(self, parent):
    super().__init__(parent)
    self.title("actualizar cliente ")
    self.build()
    self.center()
    self.transient(parent)
    self.grab_set()
      
  def build(self):
    frame = Frame(self)
    frame.pack(padx=20, pady=10)
    
    Label(frame, text="DNI (no editable)").grid(row=0, column=0)
    Label(frame, text="Nombre (de 2 a 30 chars)").grid(row=0, column=1)
    Label(frame, text="Apellido (de 2 a 30 chars)").grid(row=0, column=2)
    
    dni = Entry(frame)
    dni.grid(row=1, column=0)
    
    nombre = Entry(frame)
    nombre.grid(row=1, column=1)
    nombre.bind("<KeyRelease>", lambda event: self.validate(event, 0))
    
    apellido = Entry(frame)
    apellido.grid(row=1, column=2)
    apellido.bind("<KeyRelease>", lambda event: self.validate(event, 1))
    
    frame = Frame(self)
    frame.pack(pady=10)
    
    actualizar = Button(frame, text="Crear", command=self.edit_client)
    actualizar.grid(row=0, column=0)
    Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)
    
    
    self.validaciones = [1,1]
    self.actualizar = actualizar
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    
  def edit_client(self):
    #TODO
    self.close()
  
  def close(self):
    self.destroy()
    self.update()

  def validate(self, event, index):
    
    valor = event.widget.get()
    if index == 0:
      valido = helpers.dni_valido(valor, db.Clientes.lista)
      if valido:
        event.widget.configure({"bg":"Green"})
        self.validaciones[index] = valido
      else:
        event.widget.configure({"bg":"Red"})
    if index == 1:
      valido = valor.isalpha() and len(valor) >= 2 and len(valor) <=30
      if valido:
        event.widget.configure({"bg":"Green"})
        self.validaciones[index] = valido
      else:
        event.widget.configure({"bg":"Red"})
    if index == 2:
      valido = valor.isalpha() and len(valor) >= 2 and len(valor) <=30
      if valido:
        event.widget.configure({"bg":"Green"})
        self.validaciones[index] = valido
      else:
        event.widget.configure({"bg":"Red"})
        self.crear.config(state=NORMAL if self.validaciones == [1,1,1] else DISABLED)  
        
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
    Button(frame, text="Crear", command=self.create).grid(row=0, column=0)
    Button(frame, text="Modificar", command=self.edit).grid(row=0, column=1)
    Button(frame, text="Borrar", command=self.delete).grid(row=0, column=2)

    #boton de borrar 
    
    self.treeview = treeview
    
  #esta funcion se ejecutara al presionar el boton de borrar  
  def delete(self):
    
    #haremos uso del metodo focus que se pone en marcha 
      #cuando seleccionamos una fila de la tabla 
    #entonces aprovecharemos este metodo para poder borrar los datos
    cliente = self.treeview.focus()
    if cliente:
      #traemos los valores 
      campos = self.treeview.item(cliente, "values")
      #ventana emergente que nos pregunta si hacer o no la accion
        #personalizamos los parametros de esta funcion
      confirmar = askokcancel(
        title="Confirmar borrado",
        message=f"Borrar {campos[1]},{campos[2]}?",
        icon=WARNING
      )
      if confirmar:
        self.treeview.delete(cliente)
        
    
    #creamos instancia de la subventana 
    
  def create(self):
    CreateClientWindow(self)
    
  def edit(self):
    EditClientWindow(self)
    
if __name__ == "__main__":
  app = MainWindow()
  app.mainloop()