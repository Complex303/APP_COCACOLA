# Importamos el módulo tkinter con el alias tk para crear interfaces gráficas
import tkinter as tk
from clase_conexion import Conexion  # Importa la clase de conexión que nos va a permitir conectarnos a la bd
from tkinter import messagebox # Importamos el módulo messagebox desde tkinter para mostrar mensajes emergentes
from Licencia import Licencia # Importamos la clase Licencia desde el archivo Licencia.py

# Definimos una clase llamada Bienvenida
class Bienvenida: 
    def __init__(self): # Método constructor de la clase
        self.ventana = tk.Tk() # Creamos una ventana principal
        self.ventana.title('Acceso') # Establece el título de la ventana.
        self.ventana.iconbitmap(r'C:\App_vacaciones\imagenes\icon0.ico')  # Asignamos un ícono a la ventana
        self.ventana.resizable(False,False) # Deshabilitamos el redimensionamiento de la ventana
        self.ventana.config(bg = 'red') # Configuramos el color de fondo de la ventana
        self.ventana.geometry('350x450+600+200') # Definimos las dimensiones y posición de la ventana

        self.fondo = tk.PhotoImage(file = r'C:\App_vacaciones\imagenes\logo-coca.png') # Carga una imagen de fondo
        self.label_fondo = tk.Label(self.ventana, image = self.fondo, bg = 'red').pack() # Crea un label (etiqueta) para mostrar la imagen de fondo y lo añade a la ventana. .pack() se utiliza para colocar el label_fondo, que es una etiqueta con una imagen de fondo, en la ventana principal. Al no especificar opciones adicionales, .pack() coloca la etiqueta en la parte superior central de la ventana y ajusta el tamaño de la ventana para acomodar la imagen.

        #Labels
        self.label1 = tk.Label(self.ventana, text = 'Sistema de control vacacional') # Crea una etiqueta con el texto "Sistema de control vacacional".
        self.label1.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 18, 'italic')) # Configura el color de la fuente, el fondo, la fuente, el tamaño y el estilo del texto. 'Andale Mono Regular': Es el nombre de la fuente que se va a utilizar. el 18 es el tamaño y 'italic': Es el estilo de la fuente, en este caso, cursiva
        self.label1.place(x = 10, y = 140)  # Coloca la etiqueta en una posición específica dentro de la ventana.
        self.label2 = tk.Label(self.ventana, text = 'Ingrese su nombre:')  # Crea otra etiqueta con el texto "Ingrese su nombre:".
        self.label2.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 12, 'bold')) #'bold': Especifica que el estilo de la fuente debe ser negrita.
        self.label2.place(x = 100, y = 230)  # Coloca la etiqueta en una posición específica dentro de la ventana.

        self.label3 = tk.Label(self.ventana, text = '©2022 The Coca-Cola Company.')  # Crea otra etiqueta con el texto "©2022 The Coca-Cola Company."
        self.label3.config(font = ('Andale Mono Regular', 10, 'bold'),bg = 'red', fg = 'white' )
        self.label3.place(x = 70, y = 420)

        #entry nombre usuario
        self.dato1 = tk.StringVar() # Crea un objeto StringVar para almacenar el texto introducido por el usuario. StringVar() es una clase en Tkinter que se utiliza para gestionar valores de tipo cadena (str). Es una de las varias variables de control proporcionadas por Tkinter, que también incluye IntVar(), DoubleVar(), y BooleanVar()
        self.entry1 = tk.Entry(self.ventana, bd =2, bg = '#eee8e8', fg = 'red', textvariable= self.dato1) # Crea un campo de entrada de texto. esto es un color: #eee8e8'  es un tono muy claro de gris rosado
        self.entry1.config(font = ('Andale Mono Regular', 12, 'bold'), width= 27) # Configura la fuente, el tamaño y el estilo del texto del campo de entrada. width es el ancho del cuadro de texto
        self.entry1.place(x = 50, y = 255) # Coloca el campo de entrada en una posición específica dentro de la ventana.

        #botton
        self.boton1 = tk.Button(self.ventana, text = 'Ingresar', bd = 2, fg = 'red', bg = 'white', command= self.acceso)  # Crea un botón con el texto "Ingresar". bd es el borde
        self.boton1.config(font = ('Andale Mono Regular', 14), width = 12) # Configura la fuente, el tamaño y el estilo del texto del botón.
        self.boton1.place(x = 100, y = 295) # Coloca el botón en una posición específica dentro de la ventana
        
        self.ventana.mainloop()    # Inicia el bucle principal de la ventana.

# Definimos una función llamada "acceso"
    def acceso(self):
        nombre_usuario = self.dato1.get() #creo una variable que va a ser igual al entry donde se pone el usuario
        self.largo = self.dato1.get()  # Obtenemos el valor del campo de entrada (nombre de usuario)
        if not self.dato1.get():  # Si no se ingresó ningún nombre de usuario, mostramos un mensaje de error
            messagebox.showerror('ATENCION', 'DEBE COLOCAR NOMBRE DE USUARIO')
        elif len(self.largo) > 0 and len(self.largo) < 8:  # Si el nombre de usuario tiene menos de 8 caracteres, mostramos otro mensaje de error
            messagebox.showerror('ATENCION', 'EL NOMBRE DE USUARIO DEBE TENER MAS DE 8 CARACTERES')
        else: #si el campo no esta vacio y no tiene menos de 8 caracteres, creamos un objeto de la clase conexion (la conexion que establecimos ahorita)
            conn = Conexion() # Crear una instancia de la clase Conexion
            conn.conectar() #llamamos a la funcion o metodo conectar, que es donde establece la conexión con la base de datos.
            if conn.conn: # Verificamos si la conexión fue exitosa. La línea if conn.conn: comprueba si la conexión a la base de datos se ha establecido correctamente. Si conn.conn no es None, se considera que la conexión es válida y el programa puede proceder a ejecutar consultas en la base de datos. Si conn.conn es None, significa que la conexión falló y se muestra un mensaje de error
                try: 
                    conn.cursor.execute('SELECT N_Usuario FROM Usuario') # Ejecutamos una consulta para obtener todos los nombres de usuario de la tabla "Usuario".
                    usuarios = [] # Inicializa una lista vacía llamada 'usuarios'
                    for row in conn.cursor.fetchall(): # Itera sobre cada fila devuelta por la consulta ejecutada en el cursor de la conexión
                        usuarios.append(row[0]) # Agrega el primer elemento de cada fila a la lista 'usuarios'. # row[0] siempre accede al primer elemento de cada tupla (no cambia a row[1] en la siguiente iteración
                    if nombre_usuario in usuarios: # Comprobamos si el nombre de usuario que esta en el entry está en la lista de usuarios obtenida de la bd.
                        conn.mensaje() # Si el nombre de usuario está en la lista, mostramos un mensaje de conexión exitosa
                        self.ventana.destroy() # y cerramos la ventana actual para abrir la ventana de licencia.
                        Licencia()
            
                    else: # Si el nombre de usuario no está en la lista, mostramos un mensaje de error.
                        messagebox.showerror('ATENCIÓN', 'USUARIO NO ENCONTRADO')
                except Exception as e: # Si ocurre un error al ejecutar la consulta, mostramos un mensaje de error.
                    messagebox.showerror('ATENCIÓN', f'Error al verificar el usuario: {e}')
                finally: # En cualquier caso, cerramos la conexión a la base de datos. # Este bloque se ejecuta siempre, ocurra o no una excepción en el bloque try # Aquí se cierra la conexión a la base de datos para liberar recursos
                    conn.cerrar()
            else: # Si no se pudo establecer la conexión, mostramos un mensaje de error.
                messagebox.showerror('ATENCIÓN', 'Error al conectar a la base de datos')

if __name__ == '__main__': #if __name__ == '__main__': se utiliza para determinar si un script de Python se está ejecutando directamente o si se está importando como un módulo en otro script.
    Ejecutar = Bienvenida() ##Si este archivo se ejecuta directamente (no se importa como módulo), creamos una instancia de Bienvenida