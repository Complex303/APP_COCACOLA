import re # Importar el módulo de expresiones regulares de Python. esto se utiliza para indicar que no se admitan caracteres especiales
import sys # Importar el módulo de funcionalidades del sistema de Python esto se utilizo para salir del sistema
import tkinter as tk
from tkinter import messagebox #Importa el módulo messagebox de tkinter para mostrar diálogos emergentes.
from tkinter import ttk # importa el módulo ttk de la biblioteca tkinter# ttk es un módulo que proporciona acceso a la biblioteca de widgets temáticos de Tk para Tkinter
# Estos widgets permiten crear una interfaz gráfica con un aspecto más moderno y con estilos que pueden ser personalizados. para este caso se utiliza para crear un combobox

class principal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana Principal")
        self.ventana.resizable(False, False)
        self.ventana.geometry('650x550+410+150')
        self.ventana.config(bg = 'red')
        self.ventana.iconbitmap(r'C:\App_vacaciones\imagenes\icon0.ico')

        #menu de opciones:
        # Crea una barra de menú.
        self.menubar1 = tk.Menu(self.ventana)
        self.ventana.config(menu = self.menubar1)  # Asigna la barra de menú a la ventana.

        
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0) # Crea un menú desplegable dentro de la barra de menú.
        self.menubar1.add_cascade(label = 'Opciones', menu = self.opciones1)  # Añade el menú desplegable a la barra de menú con la etiqueta 'Opciones'.
        self.opciones1.add_command(label = 'Salir', command = self.salir, font = ('Arial', 10, 'bold')) # Añade un comando al menú desplegable 'Opciones' con la etiqueta 'Salir'.

        # Crea otro menú desplegable dentro de la barra de menú.
        self.opciones2 = tk.Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label = 'Acerca de..', menu = self.opciones2)
        self.opciones2.add_command(label = 'Info', command= self.acerca, font = ('Arial', 10, 'bold'))

        #imagen logo. # Cargamos una imagen de fondo desde el archivo "coca-cola-p.png" y la colocamos en la ventana
        self.fondo = tk.PhotoImage(file = 'C:\App_vacaciones\imagenes\coca-cola-p.png')
        self.label_fondo = tk.Label(self.ventana, image = self.fondo, bg = 'red').place(x = 0, y = 0)

        #label bienvenida.  # Creamos etiquetas de bienvenida y detalles
        self.l_bienvenida = tk.Label(self.ventana, text = 'Bienvenid@!')
        self.l_bienvenida.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 20, 'bold'))
        self.l_bienvenida.place(x = 340, y = 30)

        #label detalle
        self.l_detalle = tk.Label(self.ventana, text = 'Datos del trabajor para el calculo de vacaciones')
        self.l_detalle.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 18, 'bold'))
        self.l_detalle.place(x = 20, y = 120)

        #label nombre completo
        self.l_nombre = tk.Label(self.ventana, text = 'Nombre completo')
        self.l_nombre.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 11, 'bold'))
        self.l_nombre.place(x = 30, y = 180)

        #entry nombre completo
        self.datonombre = tk.StringVar() # Creación de una variable de control para almacenar el nombre completo
        self.e_nombre = tk.Entry(self.ventana, bd = 2, bg = '#eee8e8', fg = 'red', textvariable=self.datonombre)
        self.e_nombre.config(font = ('Andale Mono Regular', 12, 'bold'), width= 22)
        self.e_nombre.place(x = 30, y = 205)

        #label primer apellido
        self.l_p_apellido = tk.Label(self.ventana, text = 'Primer apellido') 
        self.l_p_apellido.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 11, 'bold'))
        self.l_p_apellido.place(x = 30, y = 240)

        #entry primer apellido
        self.datopapellido = tk.StringVar() # Variable para almacenar el texto ingresado
        self.e_p_apellido = tk.Entry(self.ventana, bd = 2, bg = '#eee8e8', fg = 'red', textvariable= self.datopapellido)
        self.e_p_apellido.config(font = ('Andale Mono Regular', 12, 'bold'), width= 22)
        self.e_p_apellido.place(x = 30, y = 265)

        #label segundo apellido
        self.l_s_apellido = tk.Label(self.ventana, text = 'Segundo apellido')
        self.l_s_apellido.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 11, 'bold'))
        self.l_s_apellido.place(x = 30, y = 300)

        #entry segundo apallido
        self.datosapellido = tk.StringVar()
        self.e_s_apellido = tk.Entry(self.ventana, bd = 2, bg = '#eee8e8', fg = 'red', textvariable= self.datosapellido)
        self.e_s_apellido.config(font = ('Andale Mono Regular', 12, 'bold'), width= 22)
        self.e_s_apellido.place(x = 30, y = 325)

        #select departamento
        self.l_departamento = tk.Label(self.ventana, text = 'Seleccione departamento')
        self.l_departamento.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 11, 'bold'))
        self.l_departamento.place(x = 350, y = 180)
        
        # Combobox para seleccionar el departamento. Un ComboBox es un widget de interfaz gráfica que combina una caja de texto con una lista desplegable. Permite a los usuarios seleccionar una opción de la lista o escribir una nueva entrada
        self.var_combo1 = tk.StringVar() # Creación de una variable de control para almacenar la selección del ComboBox
        self.op_combo = (' ', 'Atencion al cliente', 'Departamento de Logística', 'Departamento de Gerencia') # Lista de opciones
        self.combobox1 = ttk.Combobox(self.ventana, state = 'readonly', width= 22, # 'state' se establece en 'readonly' para que el usuario no pueda ingresar texto, solo seleccionar de la lista. # 'width' define el ancho del ComboBox
                                      font = ('Andale Mono Regular', 9, 'bold'),
                                      textvariable= self.var_combo1, values= self.op_combo)  # 'textvariable' es la variable de control que se actualiza con la selección del usuario. # 'values' son las opciones que el usuario puede seleccionar en el ComboBox
        self.combobox1.current(0) # Establece la opción predeterminada que se muestra en el ComboBox al iniciar la interfaz. El índice '0' se refiere al primer elemento de la lista de opciones del ComboBox, en este caso ' '.
        self.combobox1.place(x = 350, y = 205  )


         #select antiguedad.  # Combobox para seleccionar la antigüedad
        self.l_antiguedad = tk.Label(self.ventana, text = 'Seleccione la antiguedad')
        self.l_antiguedad.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 11, 'bold'))
        self.l_antiguedad.place(x = 350, y = 240)

        self.var_combo2 = tk.StringVar()
        self.op_combo2 = (' ', '1 año de servicio', '2 a 6 años de servicio', '7 o mas años de servicio')
        self.combobox2 = ttk.Combobox(self.ventana, state = 'readonly', width= 22,
                                      font = ('Andale Mono Regular', 9, 'bold'),
                                      textvariable= self.var_combo2, values= self.op_combo2)
        self.combobox2.current(0) # Establece el primer valor por defecto
        self.combobox2.place(x = 350, y = 265)

        # Configuración del estilo de los combobox
        estilo = ttk.Style()
        estilo.theme_use('clam') # Selección del tema 'clam' para el estilo, que es uno de los temas disponibles en Tkinter
        estilo.configure('TCombobox', background = 'red') # Configuración del estilo para los ComboBox (TCombobox) con un fondo rojo, esto es para poner la flechas de color rojo


        #label resultado
        self.l_resultado = tk.Label(self.ventana, text = 'Resultado del calculo')
        self.l_resultado.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 11, 'bold'))
        self.l_resultado.place(x = 350, y = 305)

        #texto resultado. # Creación de un área de texto para mostrar el resultado del cálculo, 'disable es para que no se puede modificar el contenido'
        self.area_resultado = tk.Text(self.ventana, bd = 2, font = ('Andale Mono Regular', 10, 'bold'))
        self.area_resultado.config(bg = '#eee8e8', fg = 'red', width= 40, height = 7, state = 'disabled')
        self.area_resultado.place(x = 350, y = 340)
        
        #label pie de interfaz. Creación de una etiqueta para el pie de la interfaz
        self.l_footer = tk.Label(self.ventana, text = '2022 The Coca-Cola Company.')
        self.l_footer.config(fg = 'White', bg = 'red', font = ('Andale Mono Regular', 10, 'bold'))
        self.l_footer.place(x = 220, y = 500)

        #botones. Creación de botones para calcular y limpiar los campos de entrada
        self.b_calcular = tk.Button(self.ventana, text = 'Calcular', bd = 5, width= 8, height = 2, command = self.control_datos)
        self.b_calcular.config(font = ('Andale Mono Regular', 12, 'bold'), bg = 'red', fg = 'white')
        self.b_calcular.place(x = 135, y = 380)

        self.b_limpiar = tk.Button(self.ventana, text = 'Limpiar', bd = 5, width= 8, height = 2, command = self.limpiadatos)
        self.b_limpiar.config(font = ('Andale Mono Regular', 12, 'bold'), bg = 'red', fg = 'white')
        self.b_limpiar.place(x = 30, y = 380)
        
        
        self.ventana.mainloop() # Inicia el bucle principal de la ventana, que la mantiene abierta.

    #las funciones de este tipo se declaran en la misma clase, pero fuera de la ventana principal. Esta función valida que todos los campos estén llenos y no excedan la longitud permitida antes de continuar.
    def control_datos(self):  # Verifica si alguno de los campos requeridos está vacío o si los combobox tienen el valor por defecto
        if not self.datonombre.get() or not self.datopapellido.get() or not self.datosapellido.get() \
            or self.var_combo1.get() == ' ' or self.var_combo2.get() == ' ':
            messagebox.showerror('AVISO', 'NO DEBEN QUEDAR CAMPOS VACIOS') # Si alguna de las condiciones anteriores es verdadera, muestra un mensaje de error.
        if len(self.datonombre.get()) > 15 or len(self.datopapellido.get()) >15 or len(self.datosapellido.get()) > 15: # Verifica si la longitud de los nombres o apellidos es mayor que 15 caracteres.
            messagebox.showerror('AVISO', 'NOMBRE / APELLIDO(S) MUY LARGOS') # Si alguna de las condiciones anteriores es verdadera, muestra un mensaje de error.
        
        pattern = re.compile(r'^[a-zA-Z0-9_]*$') # Verificar si los campos contienen solo caracteres permitidos (letras, números y _)
        if not pattern.match(self.datonombre.get()) or not pattern.match(self.datopapellido.get()) \
                or not pattern.match(self.datosapellido.get()):
            messagebox.showerror('AVISO', 'LOS CAMPOS NO PUEDE CONTENER CARACTERES ESPECIALES')
            return
        else: 
            self.area_resultado.config(state = 'normal') # Habilita el área de texto para permitir la edición
            self.area_resultado.delete('1.0', 'end') # Borra todo el contenido del área de texto
            if self.var_combo1.get() == 'Atencion al cliente': # Comprobación del departamento seleccionado y cálculo de días de vacaciones. osea lo que se hace en todos estos if es que dependiendo del departamento y antiguiedad va calcular las vacaciones
                if self.var_combo2.get() == '1 año de servicio':  # Verificación de la antigüedad y cálculo de vacaciones
                    #se inserta en el cuadro de texto el nombre los apellido el departamento seleccionado y la antiguidad.
                    self.area_resultado.insert('insert', self.datonombre.get()+' '+self.datopapellido.get()+\
                                               ' '+self.datopapellido.get()+\
                                               '\nDepartamento: '+ self.var_combo1.get()+\
                                               '\nAntiguedad: '+ self.var_combo2.get()+\
                                               '\n\nRECIBE 14 DIAS DE VACACIONES')
                if self.var_combo2.get() == '2 a 6 años de servicio':
                    self.area_resultado.insert('insert', self.datonombre.get() + ' ' + self.datopapellido.get() + ' ' + self.datosapellido.get() + \
                                               '\nDepartamento: ' + self.var_combo1.get() + \
                                               '\nAntigüedad:' + self.var_combo2.get() + \
                                               '\n\nRECIBE 18 DIAS DE VACACIONES')
                if self.var_combo2.get() == '7 o mas años de servicio':
                    self.area_resultado.insert('insert', self.datonombre.get() + ' ' + self.datopapellido.get() + ' ' + self.datosapellido.get() + \
                                               '\nDepartamento: ' + self.var_combo1.get() + \
                                               '\nAntigüedad: ' + self.var_combo2.get() + \
                                               '\n\nRECIBE 22 DIAS DE VACACIONES')
            if self.var_combo1.get() == 'Departamento de Logística': # Verificación de la antigüedad y cálculo de vacaciones
                if self.var_combo2.get() == '1 año de servicio':
                    self.area_resultado.insert('insert',
                                               self.datonombre.get() + ' ' + self.datopapellido.get() + ' ' + self.datosapellido.get() + \
                                               '\nDepartamento: ' + self.var_combo1.get() + \
                                               '\nAntigüedad: ' + self.var_combo2.get() + \
                                               '\n\nRECIBE 10 DIAS DE VACACIONES')
                if self.var_combo2.get() == '2 a 6 años de servicio':
                    self.area_resultado.insert('insert',
                                               self.datonombre.get() + ' ' + self.datopapellido.get() + ' ' + self.datosapellido.get() + \
                                               '\nDepartamento: ' + self.var_combo1.get() + \
                                               '\nAntigüedad: ' + self.var_combo2.get() + \
                                               '\n\nRECIBE 15 DIAS DE VACACIONES')
                if self.var_combo2.get() == '7 o mas años de servicio': 
                    self.area_resultado.insert('insert',
                                               self.datonombre.get() + ' ' + self.datopapellido.get() + ' ' + self.datosapellido.get() + \
                                               '\nDepartamento: ' + self.var_combo1.get() + \
                                               '\nAntigüedad: ' + self.var_combo2.get() + \
                                               '\n\nRECIBE 20 DIAS DE VACACIONES')
            if self.var_combo1.get() == 'Departamento de Gerencia': 
                if self.var_combo2.get() == '1 año de servicio': # Verificación de la antigüedad y cálculo de vacaciones
                    self.area_resultado.insert('insert',
                                               self.datonombre.get() + ' ' + self.datopapellido.get() + ' ' + self.datosapellido.get() + \
                                               '\nDepartamento: ' + self.var_combo1.get() + \
                                               '\nAntigüedad: ' + self.var_combo2.get() + \
                                               '\n\nRECIBE 18 DIAS DE VACACIONES')
                if self.var_combo2.get() == '2 a 6 años de servicio':
                    self.area_resultado.insert('insert',
                                               self.datonombre.get() + ' ' + self.datopapellido.get() + ' ' + self.datosapellido.get() + \
                                               '\nDepartamento: ' + self.var_combo1.get() + \
                                               '\nAntigüedad: ' + self.var_combo2.get() + \
                                               '\n\nRECIBE 25 DIAS DE VACACIONES')
                if self.var_combo2.get() == '7 o mas años de servicio':
                    self.area_resultado.insert('insert',
                                               self.datonombre.get() + ' ' + self.datopapellido.get() + ' ' + self.datosapellido.get() + \
                                               '\nDepartamento: ' + self.var_combo1.get() + \
                                               '\nAntigüedad: ' + self.var_combo2.get() + \
                                               '\n\nRECIBE 30 DIAS DE VACACIONES')
            self.area_resultado.config(state='disabled')  # Deshabilita el área de texto para evitar edición adicional, esto para cuando se haga el calculo no se puede modificar nada de los que esta en el cuadro

    def acerca(self): # Muestra una ventana de información con detalles del sistema, y se lo asociamos en la parte de acerca de.. en el menu
        messagebox.showinfo('INFO', '''        SISTEMA DE CONTROL DE VACACIONES
        DESARROLLADO POR: EDDY UREÑA HERNANDEZ©
        DERECHO RESERVADO 2024''')
    
    def salir(self): # Pregunta al usuario si desea salir del sistema
        seleccion = messagebox.askokcancel('SALIR', 'DESEA SALIR DEL SISTEMA?')
        if seleccion == True:
            sys.exit()


    def limpiadatos(self):
         # Habilita y limpia el área de resultado. Limpia el área de resultados y los campos de entrada, y resetea los comboboxes
        self.area_resultado.config(state = 'normal') #habilito el cuadro de resultado para poder hacer modificaciones 
        self.area_resultado.delete('1.0', 'end') #En estos ejemplos, delete('0', 'end') y delete('1.0', 'end') eliminan todo el contenido de los respectivos widgets Entry y Text
        self.area_resultado.config(state = 'disabled') #desabilito para que no se puede hacer modificaciones dentro del cuadro de texto
        self.e_nombre.delete('0', 'end')
        self.e_p_apellido.delete('0', 'end') 
        self.e_s_apellido.delete('0', 'end')
        self.combobox1.current(0)
        self.combobox2.current(0)
        #('0', 'end'): Se usa con Entry widgets para indicar el rango completo del texto dentro de un campo de entrada simple. ('1.0', 'end'): Se usa con Text widgets para indicar el rango completo del texto dentro de un campo de texto multilinea.

#ya que tenemos todos tenemos que empaquetarlo
#ver el video para entenderlo mejor
#pyinstaller es la herramienta que se usa para empaquetar




