import sys # que permite acceder a funciones y parámetros específicos del sistema. en este caso sys.exit() para salir del programa
import tkinter as tk
from tkinter import messagebox #Importa el módulo messagebox de tkinter para mostrar diálogos emergentes.
from tkinter.font import NORMAL  # Importa la constante NORMAL del módulo tkinter.font.
from Principal import principal # Importamos la clase Principal desde el archivo Principal.py

class Licencia:
    def __init__(self):
        self.ventana = tk.Tk()  # Crear la ventana principal de la aplicación.
        self.ventana.title('LICENCIA Y CONDICIONES')  # Establece el título de la ventana.
        self.ventana.resizable(False, False)  # Desactiva la capacidad de redimensionar la ventana.
        self.ventana.geometry('600x350+500+250')  # Establece el tamaño y la posición de la ventana.
        self.ventana.iconbitmap(r'C:\App_vacaciones\imagenes\icon0.ico')  # Establece el icono de la ventana.

        # Cargamos una imagen de logo y la colocamos en la ventana
        self.logo = tk.PhotoImage(file = r'C:\App_vacaciones\imagenes\coca-cola-l.png')
        self.labellogo = tk.Label(self.ventana, image = self.logo).place(x = 280, y = 200)

        #labels # Crear y configurar la etiqueta del título.
        self.label1 = tk.Label(self.ventana, text='TERMINOS Y CONDICIONES')
        self.label1.config(font=('Arial', 13, 'bold'))  # Configura la fuente de la etiqueta.
        self.label1.place(x=180, y=10)  # Coloca la etiqueta en la ventana.

        #texto. # Crear y configurar el widget de texto para mostrar los términos y condiciones.
        self.texto_condiciones = tk.Text(self.ventana, font=('Arial', 8), width=96, height=12)
        self.texto_condiciones.configure(bg='White', state='normal')  # Configura el fondo y el estado del widget de texto. El parámetro state = NORMAL se utiliza en el widget de texto (Text) en Tkinter para especificar que el campo de texto es editable y permite la entrada de texto por parte del usuario. Cuando se establece en NORMAL, el usuario puede escribir, seleccionar y modificar el contenido del campo de texto.
        # Inserta el texto de los términos y condiciones en el widget de texto. se utiliza para insertar texto en un widget de texto (Text) en Tkinter
        self.texto_condiciones.insert('insert', '''       
    TÉRMINOS Y CONDICIONES"

    A.  PROHIBIDA SU VENTA O DISTRIBUCIÓN SIN AUTORIZACIÓN DE INFORMATICONFIG.
    B.  PROHIBIDA LA ALTERACIÓN DEL CÓDIGO FUENTE O DISEÑO DE LAS INTERFACES GRÁFICAS.
    C.  INFORMATICONFIG DE ERNESTO NO SE HACE RESPONSABLE DEL MAL USO DE ESTE SOFTWARE.

    LOS ACUERDOS LEGALES EXPUESTOS A CONTINUACION RIGEN EL USO QUE USTED HAGA DE ESTE SOFTWARE
    (INFORMATICONFIG), NO SE RESPONSABILIZA DEL USO QUE USTED"
    HAGA CON ESTE SOFTWARE Y SUS SERVICIOS. PARA ACEPTAR ESTOS TERMINOS HAGA CLIC EN (ACEPTO)"
    SI USTED NO ACEPTA ESTOS TERMINOS, HAGA CLIC EN (NO ACEPTO) Y NO UTILICE ESTE SOFTWARE."
         ''')
        
        self.texto_condiciones.place(x=10, y=40)  # Coloca el widget de texto en la ventana.
        self.texto_condiciones.config(state='disabled')  # Desactiva el widget de texto para evitar modificaciones.

        #checkbuttons # Crear y configurar el Checkbutton para aceptar los términos y condiciones.
        self.acepto = tk.IntVar()  # Variable para almacenar el estado del Checkbutton. aunque si lo quito, funciona bien el programa
        self.check_acepto = tk.Checkbutton(self.ventana, text='Yo acepto', font=('Arial', 12, 'bold'), command = self.aceptar) #cada ves que se presiona sobre el chuck button, va a llamar a metodo aceptar
        self.check_acepto.place(x=10, y=230)  # Coloca el Checkbutton en la ventana.



        #buttons
        # Crear y configurar el botón de 'Acepto'. SE PONE \PARA INDICAR QUE CONTINUAREMOS ESCRIBIENDO ABAJO, PERO PORLO QUE SE VE EN EL SEGUNDO BOTON, NO ES NECESARIO
        self.boton_continuar = tk.Button(self.ventana, text = 'Acepto', font = ('Arial', 11, 'bold'),\
                                         width = 7, height = -20, bd = 3, state = 'disabled', command= self.acceso) #EL -20 ES PARA PONER LA ALTURA DEL BOTON MAS PEQUEÑO, AUNQUE CREO QUE NO ES RECOMENDABLE, EL DISABLE ES PARQ QUE NO SE PUEDE PRESIONAR EL BOTON
        self.boton_continuar.place(x = 10, y = 290)

         # Crear y configurar el botón de 'Cancelar'
        self.boton_cancelar = tk.Button(self.ventana, text = 'Cancelar', font = ('Arial', 11,'bold'),
                                        width = 7, height= -20, bd = 3, state = NORMAL, command = self.cancelar) #EL STATE AQUI NO ES NECESARIO
        self.boton_cancelar.place(x = 110, y = 290 )



        self.ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica.

    # Método para alternar el estado del botón 'boton_continuar' entre 'normal' y 'disabled'.
    def aceptar(self):
        if self.boton_continuar['state'] == 'disabled':  # Si el botón está deshabilitado, cambia su estado a 'normal' (habilitado).
            self.boton_continuar.config(state = NORMAL)
        else: # Si el botón está habilitado, cambia su estado a 'disabled' (deshabilitado).
            self.boton_continuar.config(state = 'disabled') #esto claramente hay que asociarlo al checkbuttom, osea con el command = self.aceptar

    def acceso(self): #Método para cerrar la ventana actual y llamar a la clase 'principal' que es la ventana siguiente.
        self.ventana.destroy() # Destruye la ventana actual.
        principal() # Llama a la clase principal importada del módulo Principal.

    def cancelar(self): #Método para preguntar al usuario si desea salir del sistema y, si es así, salir del programa.
        seleccion = messagebox.askokcancel('Salir', 'Desea salir del sistema?')
        if seleccion ==True:
            sys.exit() # Si el usuario confirma, cierra la aplicación
        



#nota: Si no declaras ningún constructor en tu clase, el compilador (o intérprete) crea un constructor predeterminado sin parámetros.
#Este constructor predeterminado no es visible en el código fuente, pero está presente en el bytecode generado después de la compilación.
        