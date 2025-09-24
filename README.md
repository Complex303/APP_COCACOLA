# 🏖️ Sistema de Control de Vacaciones - Coca Cola

Una aplicación de escritorio desarrollada en Python con Tkinter para calcular los días de vacaciones de empleados según su departamento y antigüedad laboral.

## 📋 Descripción

Este sistema permite a las empresas calcular automáticamente los días de vacaciones que corresponden a cada empleado basándose en:
- Departamento de trabajo
- Años de antigüedad en la empresa
- Información personal del empleado

## 🚀 Características

- **Interfaz gráfica intuitiva** con tema corporativo de Coca-Cola
- **Sistema de autenticación** con verificación de usuarios en base de datos
- **Cálculo automático** de días de vacaciones según políticas empresariales
- **Validación de datos** con control de errores
- **Conexión a base de datos SQL Server** para gestión de usuarios

## 🏢 Departamentos y Política de Vacaciones

### Atención al Cliente
- 1 año: **14 días**
- 2-6 años: **18 días**
- 7+ años: **22 días**

### Departamento de Logística
- 1 año: **10 días**
- 2-6 años: **15 días**
- 7+ años: **20 días**

### Departamento de Gerencia
- 1 año: **18 días**
- 2-6 años: **25 días**
- 7+ años: **30 días**

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Tkinter** - Interfaz gráfica
- **pyodbc** - Conexión a base de datos SQL Server
- **python-dotenv** - Manejo de variables de entorno
- **re** - Validación con expresiones regulares

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone [url-del-repositorio]
cd App_vacaciones
```

2. Instala las dependencias:
```bash
pip install pyodbc python-dotenv
```

3. Configura las variables de entorno creando un archivo `.env`:
```env
DB_DRIVER={ODBC Driver 17 for SQL Server}
DB_SERVER=tu_servidor
DB_NAME=tu_base_de_datos
```

4. Asegúrate de tener las imágenes en la carpeta `imagenes/`:
- `icon0.ico`
- `logo-coca.png`
- `coca-cola-p.png`
- `coca-cola-l.png`

## 🎮 Uso

1. Ejecuta la aplicación:
```bash
python Bienvenida.py
```

2. **Pantalla de Login**: Ingresa tu nombre de usuario (mínimo 8 caracteres)

3. **Términos y Condiciones**: Acepta los términos para continuar

4. **Pantalla Principal**:
   - Completa los datos del empleado
   - Selecciona departamento y antigüedad
   - Presiona "Calcular" para obtener los días de vacaciones
   - Usa "Limpiar" para resetear los campos

## 📁 Estructura del Proyecto

```
App_vacaciones/
├── Bienvenida.py          # Pantalla de login
├── Licencia.py            # Términos y condiciones
├── Principal.py           # Pantalla principal de cálculo
├── clase_conexion.py      # Clase para conexión a BD
├── calendario.py          # [Funcionalidad adicional]
├── .env                   # Variables de entorno (no incluir en git)
├── .gitignore            # Archivos ignorados por git
├── imagenes/             # Recursos gráficos
│   ├── icon0.ico
│   ├── logo-coca.png
│   ├── coca-cola-p.png
│   └── coca-cola-l.png
└── README.md             # Este archivo
```

## 🔧 Funcionalidades Técnicas

- **Validación de entrada**: No permite caracteres especiales, límite de caracteres
- **Conexión segura a BD**: Uso de variables de entorno para credenciales
- **Manejo de errores**: Try-catch para operaciones de base de datos
- **Interfaz responsive**: Diseño fijo optimizado para resolución estándar

## ⚠️ Requisitos del Sistema

- Windows (para conexión ODBC a SQL Server)
- Python 3.6+
- SQL Server con tabla `Usuario` que contenga columna `N_Usuario`
- Driver ODBC 17 para SQL Server

