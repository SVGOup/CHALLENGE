#CREATED BY SEBASTIAN VAZQUEZ GOMEZ O.
import os
import tkinter as tk
from tkinter import messagebox
import pyodbc
from datetime import datetime

# Función para crear una nueva base de datos de Access
def crear_nueva_basededatos(ruta_archivo):
    # Verificar si el archivo ya existe
    if os.path.exists(ruta_archivo):
        print("El archivo ya existe.")
        return
    
    # Crear una nueva base de datos de Access
    try:
        conexion = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
            f'CreateDB={ruta_archivo};'
            'DBQ='
        )
        conexion.close()
        print("Se ha creado la nueva base de datos con éxito.")
    except pyodbc.Error as err:
        print("Error al crear la base de datos:", err)

# Crear una nueva base de datos
crear_nueva_basededatos('D:\\SEBVG\\Documents\\database\\base.accdb')

# Conectar a la nueva base de datos
try:
    conexion = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=D:\\SEBVG\\Documents\\database\\base.accdb;'
    )
    cursorBD = conexion.cursor()
    print("Conexión establecida y cursor creado con éxito.")
except pyodbc.Error as err:
    print("Error al conectar a la base de datos:", err)


# --------------------------------------------USUARIO-------------------------------------------------

# Función para verificar si la tabla USUARIO existe
def tablaExisteU():
    try:
        cursorBD.execute("SELECT * FROM USUARIO")
        return True
    except pyodbc.Error as e:
        # Si se produce un error al ejecutar la consulta, asumimos que la tabla no existe
        return False

if tablaExisteU():
    # Si la tabla ya existe, eliminarla y recrearla con la estructura actualizada
    cursorBD.execute('''DROP TABLE USUARIO''')

# Crear la tabla USUARIO
cursorBD.execute('''CREATE TABLE USUARIO (CODIGO AUTOINCREMENT, NAME TEXT, CONTRASEÑA TEXT)''')

# Función para insertar usuarios
def InsertarUsuario(nombre, contraseña):
    cursorBD.execute('''INSERT INTO USUARIO (NAME, CONTRASEÑA) VALUES (?,?)''', (nombre, contraseña))
    conexion.commit()

# Función para seleccionar todos los usuarios
def seleccionarUsr():
    cursorBD.execute('''SELECT * FROM USUARIO''')
    lista = []
    for filaEncontrada in cursorBD.fetchall():
        lista.append(filaEncontrada)
    return lista

# Función para actualizar usuarios
def actualizarUSR(codigo, diccionario):
    valoresVal = ['NAME', 'CONTRASEÑA']
    for key in diccionario.keys():
        if key not in valoresVal:
            raise Exception('Esa columna no existe')
        else:
            cursorBD.execute('''UPDATE USUARIO SET {} = ? WHERE CODIGO = ?'''.format(key), (diccionario[key], codigo))
    conexion.commit()

# Insertar algunos usuarios
InsertarUsuario('SEBASTIAN', 'AB12')
InsertarUsuario('JAVIER', 'CD34')
InsertarUsuario('RICARDO', 'EF56')

# Seleccionar y mostrar los usuarios
usuarios = seleccionarUsr()
print(*usuarios)

#-----------------------------------------------------PRODUCTOS-------------------------------------------------

def tablaExistePur():
    try:
        cursorBD.execute("SELECT * FROM PRODUCTOS")
        return True
    except pyodbc.Error as e:
        # Si se produce un error al ejecutar la consulta, asumimos que la tabla no existe
        return False

if tablaExistePur():
    # Si la tabla ya existe, eliminarla y recrearla con la estructura actualizada
    cursorBD.execute('''DROP TABLE PRODUCTOS''')


cursorBD.execute('''CREATE TABLE PRODUCTOS (CODIGO AUTOINCREMENT, NAME TEXT, PRECIO REAL, PESO REAL, FECHA TEXT)''')

def InsertarPurchace(nombre, precio, peso, fecha):
    cursorBD.execute('''INSERT INTO PRODUCTOS (NAME, PRECIO, PESO, FECHA) VALUES (?,?,?,?)''', (nombre, precio, peso, fecha))
    conexion.commit()

    
InsertarPurchace('Galletas', 550, 10, '')
InsertarPurchace('Panques', 600, 20, '')
InsertarPurchace('Pasteles', 800, 25, '')

def seleccionarPch():
    cursorBD.execute('''SELECT * FROM PRODUCTOS''')
    lista = []
    for filaEncontrada in cursorBD.fetchall():
        lista.append(filaEncontrada)
    return lista

def actualizarPCH(codigo, diccionario):
    valoresVal = ['NAME', 'PRECIO', 'PESO', 'FECHA']
    for key in diccionario.keys():
        if key not in valoresVal:
            raise Exception('Esa columna no existe')
        else:
            cursorBD.execute('''UPDATE PRODUCTOS SET {} = ? WHERE CODIGO = ?'''.format(key), (diccionario[key], codigo))
    conexion.commit()

# Seleccionar y mostrar las compras
purchace = seleccionarPch()
print(*purchace)


#--------------------------------------------------REGISTRO COMPRAS--------------------------------

def tablaExisteCMPR():
    try:
        cursorBD.execute("SELECT * FROM COMPRAS")
        return True
    except pyodbc.Error as e:
        # Si se produce un error al ejecutar la consulta, asumimos que la tabla no existe
        return False

if tablaExisteCMPR():
    # Si la tabla ya existe, eliminarla y recrearla con la estructura actualizada
    cursorBD.execute('''DROP TABLE COMPRAS''')


cursorBD.execute('''CREATE TABLE COMPRAS (CODIGO AUTOINCREMENT, NAME TEXT, PRECIO REAL, PESO REAL, FECHA TEXT)''')

# Función para insertar compra
def InsertarCompra(nombre, precio, peso, fecha):
    cursorBD.execute('''INSERT INTO COMPRAS (NAME, PRECIO, PESO, FECHA) VALUES (?,?,?,?)''', 
                      (nombre, precio, peso, fecha))
    conexion.commit()

# Función para obtener la fecha y hora actual


def actualizarCMPR(codigo, diccionario):
    valoresVal = ['NAME', 'PRECIO', 'PESO', 'FECHA']
    for key in diccionario.keys():
        if key not in valoresVal:
            raise Exception('Esa columna no existe')
        else:
            cursorBD.execute('''UPDATE COMPRAS SET {} = ? WHERE CODIGO = ?'''.format(key), (diccionario[key], codigo))
    conexion.commit()

def seleccionarCmpr():
    cursorBD.execute('''SELECT * FROM COMPRAS''')
    lista = []
    for filaEncontrada in cursorBD.fetchall():
        lista.append(filaEncontrada)
    return lista

COMPRA = seleccionarCmpr()
print(*COMPRA)

def obtener_fecha_actual():
    return datetime.now().strftime('%d/%m/%Y')

def eliminar_todos_registros():
    cursorBD.execute('''DELETE FROM COMPRAS''')
    conexion.commit()
    messagebox.showinfo("Eliminación Exitosa", "Todos los registros de la tabla COMPRAS han sido eliminados correctamente")

eliminar_todos_registros()

#----------------------------------------------------CAMIONES--------------------------------------

def tablaExisteCMN():
    try:
        cursorBD.execute("SELECT * FROM CAMIONES")
        return True
    except pyodbc.Error as e:
        # Si se produce un error al ejecutar la consulta, asumimos que la tabla no existe
        return False

if tablaExisteCMN():
    # Si la tabla ya existe, eliminarla y recrearla con la estructura actualizada
    cursorBD.execute('''DROP TABLE CAMIONES''')


cursorBD.execute('''CREATE TABLE CAMIONES (CODIGO AUTOINCREMENT, CODE TEXT, MAX_PESO REAL, DISPONIBLE REAL)''')


# Función para insertar compra
def InsertarCMN(code, max_weight, available):
    cursorBD.execute('''INSERT INTO CAMIONES (CODE, MAX_PESO, DISPONIBLE) VALUES (?,?,?)''', 
                      (code, max_weight, available))
    conexion.commit()

InsertarCMN('1000', 500, 1)
InsertarCMN('1001', 500, 1)
InsertarCMN('1011', 500, 1)
InsertarCMN('1100', 500, 1)

def actualizarCMN(codigo, diccionario):
    valoresVal = ['CODE', 'MAX_PESO', 'DISPONIBLE']
    for key in diccionario.keys():
        if key not in valoresVal:
            raise Exception('Esa columna no existe')
        else:
            cursorBD.execute('''UPDATE CAMIONES SET {} = ? WHERE CODIGO = ?'''.format(key), (diccionario[key], codigo))
    conexion.commit()

def seleccionarCMN():
    cursorBD.execute('''SELECT * FROM CAMIONES''')
    lista = []
    for filaEncontrada in cursorBD.fetchall():
        lista.append(filaEncontrada)
    return lista

CAMION = seleccionarCMN()
print(*CAMION)

def eliminar_todos_registrosCMN():
    cursorBD.execute('''DELETE FROM CAMIONES''')
    conexion.commit()
    messagebox.showinfo("Eliminación Exitosa", "Todos los registros de la tabla CAMION han sido eliminados correctamente")

#-----------------------------------------------------DISPALY--------------------------------------


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Pedidos")

# Función para verificar el inicio de sesión
def iniciar_sesion():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()

    # Consultar la base de datos para verificar el usuario y la contraseña
    cursorBD.execute("SELECT * FROM USUARIO WHERE NAME=? AND CONTRASEÑA=?", (usuario, contraseña))
    resultado = cursorBD.fetchone()

    if resultado:
        # Si el usuario y la contraseña son correctos, mostrar el menú principal
        mostrar_menu_principal()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para mostrar el menú principal
def mostrar_menu_principal():
    # Ocultar el formulario de inicio de sesión
    frame_inicio_sesion.pack_forget()

    # Crear el menú principal
    frame_menu_principal = tk.Frame(ventana)
    frame_menu_principal.pack()

    # Etiqueta de bienvenida
    etiqueta_bienvenida = tk.Label(frame_menu_principal, text=f"Bienvenido, {entrada_usuario.get()}!")
    etiqueta_bienvenida.pack(pady=20)

    # Botones de las opciones del menú principal
    boton_comprar = tk.Button(frame_menu_principal, text="Comprar Productos", command=mostrar_comprar_productos)
    boton_comprar.pack(pady=5)
    
    boton_ver_codigo_viaje = tk.Button(frame_menu_principal, text="Ver Código de Viaje del Pedido", command=mostrar_codigo_viaje)
    boton_ver_codigo_viaje.pack(pady=5)
    
    boton_ver_transporte = tk.Button(frame_menu_principal, text="Ver Transporte del Pedido", command=mostrar_ver_transporte)
    boton_ver_transporte.pack(pady=5)
    
    boton_cerrar = tk.Button(frame_menu_principal, text="cerrar", command=cerrar_conexion)
    boton_cerrar.pack(pady=5)

# Funciones para mostrar las diferentes opciones del menú principal (aún por implementar)
def mostrar_comprar_productos():
    messagebox.showinfo('Productos:', '(GALLETAS, PRECIO: 550, PESO: 10KG), (PANQUES, PRECIO: 600, PESO: 20KG), (PASTELES, PRECIO: 800, PESO: 25KG)')
    
    frame_inicio_sesion.pack_forget()

    frame_compra = tk.Frame(ventana)
    frame_compra.pack(padx=10, pady=10)

    etiqueta_producto = tk.Label(frame_compra, text="Nombre del Producto:")
    etiqueta_producto.grid(row=0, column=0, sticky="e")
    entrada_producto = tk.Entry(frame_compra)
    entrada_producto.grid(row=0, column=1)

    etiqueta_precio = tk.Label(frame_compra, text="Precio:")
    etiqueta_precio.grid(row=1, column=0, sticky="e")
    entrada_precio = tk.Entry(frame_compra)
    entrada_precio.grid(row=1, column=1)

    etiqueta_peso = tk.Label(frame_compra, text="Peso:")
    etiqueta_peso.grid(row=2, column=0, sticky="e")
    entrada_peso = tk.Entry(frame_compra)
    entrada_peso.grid(row=2, column=1)

    # Obtener fecha actual
    fecha_actual = obtener_fecha_actual()

    # Función para procesar la compra
    def procesar_compra():
        nombre_producto = entrada_producto.get()
        precio = float(entrada_precio.get())
        peso = float(entrada_peso.get())

        # Obtener fecha actual
        fecha_actual = obtener_fecha_actual()

        # Insertar compra en la tabla COMPRAS
        InsertarCompra(nombre_producto, precio, peso, fecha_actual)

        # Mostrar mensaje de compra exitosa
        messagebox.showinfo("Compra Exitosa", "El producto ha sido comprado exitosamente.")

        # Limpiar los campos de entrada
        entrada_producto.delete(0, tk.END)
        entrada_precio.delete(0, tk.END)
        entrada_peso.delete(0, tk.END)

        # Obtener y mostrar todas las compras realizadas hasta ahora
        compras_realizadas = seleccionarCmpr()
        precio_total = sum(compra[2] for compra in compras_realizadas)
        mensaje = "Productos Comprados:\n"
        for compra in compras_realizadas:
            mensaje += f"{compra[1]} - Precio: ${compra[2]} - Peso: {compra[3]} - fecha: {fecha_actual}\n"
        mensaje += f"\nPrecio Total: ${precio_total}"
        messagebox.showinfo("Resumen de Compras", mensaje)

    # Botón para procesar la compra
    boton_comprar = tk.Button(frame_compra, text="Comprar", command=procesar_compra)
    boton_comprar.grid(row=4, columnspan=2, pady=10)

def mostrar_codigo_viaje():
    # Obtener las compras realizadas por el usuario
    compras_realizadas = seleccionarCmpr()

    if not compras_realizadas:
        messagebox.showinfo("Ver Código de Viaje del Pedido", "No has realizado ninguna compra aún.")
        return

    # Crear un mensaje con las compras realizadas
    mensaje_compras = "Tus compras realizadas:\n"
    for compra in compras_realizadas:
        mensaje_compras += f"Producto: {compra[1]}, Precio: ${compra[2]}, Peso: {compra[3]}\n"

    # Obtener un camión disponible
    camiones_disponibles = [camion for camion in CAMION if camion[3]]  # Filtrar camiones disponibles
    if not camiones_disponibles:
        messagebox.showwarning("Ver Código de Viaje del Pedido", "Lo sentimos, no hay camiones disponibles en este momento.")
        return

    # Tomar el primer camión disponible y asignarlo al pedido
    camion_asignado = camiones_disponibles[0]
    codigo_camion_asignado = camion_asignado[0]
    codigo_pedido = compras_realizadas[0][0]  # Tomar el código de la primera compra (puedes adaptarlo según tu lógica)

    # Actualizar el estado del camión asignado a False
    actualizarCMN(codigo_camion_asignado, {'DISPONIBLE': 0})

    # Mostrar el mensaje con las compras y la información del camión asignado
    mensaje_codigo_viaje = f"{mensaje_compras}\nCamión asignado:\nCódigo: {camion_asignado[1]}, Peso Máximo: {camion_asignado[2]} kg"
    messagebox.showinfo("Ver Código de Viaje del Pedido", mensaje_codigo_viaje)

def mostrar_ver_transporte():
    # Obtener la lista de camiones y su estado de disponibilidad
    lista_camiones = seleccionarCMN()

    if not lista_camiones:
        messagebox.showinfo("Ver Transporte del Pedido", "No hay camiones registrados.")
        return

    # Crear un mensaje con la información de los camiones y su disponibilidad
    mensaje_camiones = "Lista de Camiones:\n"
    for camion in lista_camiones:
        estado = "Disponible" if camion[3] else "No Disponible"
        mensaje_camiones += f"Código: {camion[1]}, Peso Máximo: {camion[2]} kg, Estado: {estado}\n"

    messagebox.showinfo("Ver Transporte del Pedido", mensaje_camiones)

# Crear el formulario de inicio de sesión
frame_inicio_sesion = tk.Frame(ventana)
frame_inicio_sesion.pack(padx=10, pady=10)

etiqueta_usuario = tk.Label(frame_inicio_sesion, text="Usuario:")
etiqueta_usuario.grid(row=0, column=0, sticky="e")

entrada_usuario = tk.Entry(frame_inicio_sesion)
entrada_usuario.grid(row=0, column=1)

etiqueta_contraseña = tk.Label(frame_inicio_sesion, text="Contraseña:")
etiqueta_contraseña.grid(row=1, column=0, sticky="e")

entrada_contraseña = tk.Entry(frame_inicio_sesion, show="*")
entrada_contraseña.grid(row=1, column=1)

boton_iniciar_sesion = tk.Button(frame_inicio_sesion, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar_sesion.grid(row=2, columnspan=2, pady=10)

# Función para cerrar la conexión a la base de datos cuando se cierre la ventana
def cerrar_conexion():
    conexion.close()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_conexion)

# Ejecutar la ventana principal
ventana.mainloop()
#CREATED BY SEBASTIAN VAZQUEZ GOMEZ O.