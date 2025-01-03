import pyodbc # Importamos la librería pyodbc que permite conectarse y operar con bases de datos ODBC en Python.

# Definimos una clase llamada Conexion que encapsula toda la funcionalidad relacionada con la conexión a la base de datos.
class Conexion:
    def __init__(self):  #El método constructor (__init__) se ejecuta cuando se crea una instancia de la clase.
        # Definimos la cadena de conexión que especifica el controlador de la base de datos, el servidor, la base de datos y el tipo de autenticación.
        self.cadena_conexion = '''DRIVER={SQL SERVER};
                                  Server=Go-8ZG6503\\MSSSQLSERVER_DEV;
                                  Database=Coca_Cola;
                                  Trusted_Connection=yes;'''
        # Inicializamos los atributos conn y cursor a None. Estos serán usados para almacenar la conexión y el cursor de la base de datos. NO ES NECESARIO
        self.conn = None
        self.cursor = None #El término None es un valor especial en Python que representa la ausencia de valor o la falta de definición. Es similar a otros lenguajes de programación que tienen conceptos como null o nil.

     # Definimos un método conectar que establece la conexión con la base de datos.
    def conectar(self):
        try: # Intentamos crear una conexión utilizando la cadena de conexión.
            self.conn = pyodbc.connect(self.cadena_conexion)
            self.cursor = self.conn.cursor() # Si la conexión es exitosa, creamos un cursor para ejecutar consultas SQL.
        except Exception as err: # Si ocurre un error durante la conexión, lo capturamos y mostramos un mensaje de error.
            print('Error en la conexión con SQL Server!!', err)
            self.conn = None # Además, establecemos conn a None para indicar que no hay conexión activa

    # Definimos un método mensaje que ejecuta una consulta para obtener la versión del servidor SQL.
    def mensaje(self):
        self.cursor.execute('SELECT @@VERSION') # Ejecutamos una consulta SQL para obtener la versión del servidor.
        select = self.cursor.fetchone() # Obtenemos la primera fila del resultado de la consulta.
        print('Conectado correctamente', select) # Imprimimos un mensaje indicando que la conexión fue exitosa y mostramos la versión del servidor.

    # Definimos un método cerrar que cierra el cursor y la conexión con la base de datos.
    def cerrar(self):
        if self.cursor: # Si el cursor está definido (no es None), intentamos cerrarlo. lo contrario a esto if self.cursor is None:
            try:
                self.cursor.close()
            except Exception as e: # Si ocurre un error al cerrar el cursor, lo capturamos y mostramos un mensaje de error.
                print("Error cerrando el cursor:", e)
        if self.conn: # Si la conexión está definida (no es None), intentamos cerrarla. y mostramos un mensaje de que se cerro correctamente
            try:
                self.conn.close()
                print('Conexion cerrada correctamente!!')
            except Exception as e: # Si ocurre un error al cerrar la conexión, lo capturamos y mostramos un mensaje de error.
                print("Error cerrando la conexión:", e)

#en la funcion cerrar, si pondemos self.cursor.close() y self.conn.close() funcionaria igual
#Nota: Al cerrar la conexión, también se cierra el cursor asociado. Sin embargo, es una buena práctica cerrar el cursor antes de cerrar la conexión para evitar posibles errores. 