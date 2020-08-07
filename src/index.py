# Librerias

from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import smtplib
import sqlite3

# GUI

class Tienda:

    productosdb = '.\database\productos.db'
    
    def __init__(self, app):
        
        self.ventana = app
        self.ventana.title("Gestor de productos")
        self.ventana.resizable(False, False)
        self.ventana.iconbitmap('.\ico\logo.ico')
        # Contenido

        self.contenido = LabelFrame(self.ventana, text="  Ingresar  ")
        self.contenido.grid(row=0, column=0, padx=23, pady=10, columnspan=7)

        usuario_n = Label(self.contenido, text="Usuario:").grid(row=0, column=0, pady=5, padx=5)
        self.usuario_e = Entry(self.contenido)
        self.usuario_e.focus()
        self.usuario_e.grid(row=0, column=1, pady=5, padx=5)

        clave_n = Label(self.contenido, text="Contraseña:").grid(row=1, column=0, pady=5, padx=5)
        self.clave_e = Entry(self.contenido)
        self.clave_e.grid(row=1, column=1, pady=5, padx=5)

        entrada = ttk.Button(self.contenido, text="Entrar", command=self.entrar)
        entrada.grid(row=2, column=0, pady=5, columnspan=2)

    # Función Validar

    def validar(self):

        return len(self.usuario_e.get()) != 0 and len(self.clave_e.get()) != 0

    # Entrar a la tabla

    def entrar(self):
        
        user = str(self.usuario_e.get())
        clave = str(self.clave_e.get())

        if self.validar():
            
            if (user == "admin" and clave == "1234"):

                # Limpia o borrar los datos del usuario y texto informativo

                self.advertencia = Label(self.ventana, text=("Bienvenido, " + user + "."), fg="green")
                self.advertencia.grid(row=2, column=0, columnspan=6, pady=2.5)
                self.usuario_e.delete(0, END)
                self.clave_e.delete(0, END)

                # Muestra la tabla
                
                self.tabla()

                # Botones

                self.agregar = ttk.Button(self.ventana, text="Agregar", command=self.agregar)
                self.agregar.grid(row=3, column=0, pady=10, columnspan=2)

                editar = ttk.Button(self.ventana, text="Editar", command=self.editar)
                editar.grid(row=3, column=1, pady=10, columnspan=2)

                eliminar = ttk.Button(self.ventana, text="Eliminar", command=self.eliminar)
                eliminar.grid(row=3, column=2, pady=10, columnspan=2)

                    # Soporte por correo

                soporte = ttk.Button(self.ventana, text="Soporte", command=self.soporte)
                soporte.grid(row=3, column=3, pady=10, columnspan=2)

            else:
                self.usuario_e.delete(0, END)
                self.clave_e.delete(0, END)
                self.usuario_e.focus()
        else:
            self.usuario_e.delete(0, END)
            self.clave_e.delete(0, END)
            self.usuario_e.focus()

    # Coneción base de datos de productos

    def consulta(self, consultas, parametros =()):
        
        with sqlite3.connect(self.productosdb) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(consultas, parametros)
            conn.commit()
        return resultado

    def atraer_productos(self):
        
        # Limpia la tabla para agregar nuevos datos

        elementos = self.tree.get_children()
        for element in elementos:
            self.tree.delete(element)

        # Lee y trae los productos

        consultas = 'SELECT * FROM productos'
        filas = self.consulta(consultas)
        for row in filas:
            self.tree.insert('', 0, values=row)

    # Crea tabla de productos

    def tabla(self):

        self.productos = LabelFrame(self.ventana, text="  Productos  ")
        self.productos.grid(row=1, column=0, padx=23, columnspan=5)

        # Tabla ver prodcutos

        tabla = Label(self.productos)
        tabla.grid(row=1, column=0, columnspan=5)

        self.tree = ttk.Treeview(tabla, height=10, columns=(1,2,3), show="headings")
        self.tree.grid(row=3, column=0, columnspan=5)
        self.tree.heading(1, text="Nombre", anchor=CENTER)
        self.tree.heading(2, text="Cantidad", anchor=CENTER)
        self.tree.heading(3, text="Precio", anchor=CENTER)

        self.atraer_productos()

    # Agregar productos

    def agregar(self):

        self.advertencia['text'] = ("")
        self.guarda = Toplevel()
        self.guarda.resizable(False, False)
        self.guarda.title("Agregar Producto")
        self.guarda.iconbitmap('.\ico\guarda.ico')

        guarda_1 = LabelFrame(self.guarda, text="  Agregar  ")
        guarda_1.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        nombre = Label(guarda_1, text="Nombre:").grid(row=0, column=0, padx=2.5, pady=5)
        self.nombre = Entry(guarda_1)
        self.nombre.focus()
        self.nombre.grid(row=0, column=1, padx=5, pady=5)

        cantidad = Label(guarda_1, text="Cantidad:").grid(row=1, column=0, padx=2.5, pady=5)
        self.cantidad = Entry(guarda_1)
        self.cantidad.grid(row=1, column=1, padx=5, pady=5)

        precio = Label(guarda_1, text="Precio:").grid(row=2, column=0, padx=2.5, pady=5)
        self.precio = Entry(guarda_1)
        self.precio.grid(row=2, column=1, padx=5, pady=5)

        guarda_2 = ttk.Button(guarda_1, text="Agregar", command=self.agregar_produtos)
        guarda_2.grid(row=3, column=0, columnspan=2, pady=2.5)

    def agregar_produtos(self):

        def agregar_validar():

            return len(self.nombre.get()) != 0

        if agregar_validar():
            consultas = 'INSERT INTO productos VALUES(?,?,?)'
            datos = (self.nombre.get(), self.cantidad.get(), self.precio.get())
            self.consulta(consultas, datos)
            self.atraer_productos()

            self.advertencia['text'] = (str(self.nombre.get()) + ", agregado correctamente.")
            self.advertencia['fg'] = ("green")

            self.nombre.delete(0, END)
            self.cantidad.delete(0, END)
            self.precio.delete(0, END)

            self.nombre.focus()

        else:
            self.advertencia['text'] = ("Agregar datos al nuevo producto.")
            self.advertencia['fg'] = "red"
            self.nombre.focus()

    def editar(self):

        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError:
            self.advertencia['text'] = ("¡Por favor seleccione un producto!")
            self.advertencia['fg'] = ("red")
            return

        self.advertencia['text'] = ""
        self.edita = Toplevel()
        self.edita.title("Editar producto")
        self.edita.resizable(False, False)
        self.edita.iconbitmap('.\ico\editar.ico')

        editar = LabelFrame(self.edita, text=("  Editar " + str(self.tree.item(self.tree.selection())['values'][0])) + "  ")
        editar.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        nombre_edi = Label(editar, text="Nombre:").grid(row=0, column=0, pady=5, padx=2.5)
        self.nombre_edi = Entry(editar)
        self.nombre_edi.focus()
        self.nombre_edi.grid(row=0, column=1, pady=5, padx=2.5)

        cantidad_edi = Label(editar, text="Cantidad:").grid(row=1, column=0, padx=2.5, pady=5)
        self.cantidad_edi = Entry(editar)
        self.cantidad_edi.grid(row=1, column=1, padx=5, pady=5)

        precio_edi = Label(editar, text="Precio:").grid(row=2, column=0, padx=2.5, pady=5)
        self.precio_edi = Entry(editar)
        self.precio_edi.grid(row=2, column=1, padx=5, pady=5)

        name = self.tree.item(self.tree.selection())['values'][0]

        guarda_3 = ttk.Button(editar, text="Guardar", command=lambda: self.editar_guarda(name))
        guarda_3.grid(row=3, column=0, columnspan=2, pady=2.5)

        self.edita.mainloop()


    def editar_guarda(self, name):

        def validar_editar():
            return len(self.nombre_edi.get()) !=0 and len(self.cantidad_edi.get()) !=0 and len(self.precio_edi.get()) !=0

        if validar_editar():
            
            consultas = 'UPDATE productos SET nombre = ?, cantidad = ?, precio = ? WHERE nombre = ?'
            datos = (self.nombre_edi.get(), self.cantidad_edi.get(), self.precio_edi.get(),name)
            self.consulta(consultas, datos)
            self.atraer_productos()
            self.advertencia['text'] = ("Datos editados correctamente.")
            self.advertencia['fg'] = "green"
            
            def cerrar():
                self.edita.destroy()
                self.edita.update()
            
            cerrar()
        else:
            self.nombre_edi.focus()
            self.advertencia['text'] = ("Agregar datos para editar.")
            self.advertencia['fg'] = "red"

    # Eliminar productos
    
    def eliminar(self):
        
        try:
            self.tree.item(self.tree.selection())['values'][0]

        except IndexError as e:
            self.atraer_productos()
            self.advertencia['fg'] = ("red")
            self.advertencia['text'] = ("¡Por favor seleccione un producto!")
            return

        self.advertencia['fg'] = ("green")
        self.advertencia['text'] = ((self.tree.item(self.tree.selection())['values'][0]) +", eliminado correctamente.")
        
        nombre = (self.tree.item(self.tree.selection())['values'][0])
        consultas = 'DELETE FROM productos WHERE nombre = ?'
        self.consulta(consultas, (nombre,))
        self.atraer_productos()

    # Soporte, enviar correo registrar usuarios

    def soporte(self):

        self.advertencia['text'] = ("")
        self.soporte = Toplevel()
        self.soporte.title("Soporte")
        self.soporte.resizable(False, False)
        self.soporte.iconbitmap('.\ico\soporte.ico')

        self.enviar = LabelFrame(self.soporte, text="  Enviar  ")
        self.enviar.grid(row=0, column=0, pady=10, padx=10)

        info = Label(self.enviar, text="Comunicate por medio de correo eletronico.")
        info.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        asunto = Label(self.enviar, text="Asunto:").grid(row=1, column=0, pady=10)
        self.asunto_e = Entry(self.enviar)
        self.asunto_e.focus()
        self.asunto_e.grid(row=1, column=1, pady=10)

        text = Label(self.enviar, text="Mensaje:").grid(row=2, column=0, pady=10)
        self.text_e = Entry(self.enviar)
        self.text_e.grid(row=2, column=1, pady=10)

        enviar_b = ttk.Button(self.enviar, text="Enviar", command=self.enviar_m)
        enviar_b.grid(row=5, column=0, pady=10, columnspan=2)

    def enviar_m(self):

        def enviar_validar():

            return len(self.asunto_e.get()) != 0 and len(self.text_e.get()) != 0

        if enviar_validar():

            try:
                smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo()
                smtpserver.login('correo_e', 'contraseña_e')

                subject = str(self.asunto_e.get())
                mensanje = str(self.text_e.get())

                mensanje = 'Subject: {}\n\n{}'.format(subject, mensanje)

                smtpserver.sendmail('correo_e', 'enviar_a', mensanje)
                smtpserver.quit()
                e = "     Enviado correctamente.     "
                Label(self.enviar, text=e, fg='green').grid(row=4, column=0, columnspan=2, pady=2.5)
                self.asunto_e.delete(0, END)
                self.text_e.delete(0, END)
                self.asunto_e.focus()

            except:
                error = "         ¡Errores al enviar!         "
                Label(self.enviar, text=error, fg='red').grid(row=4, column=0, columnspan=2, pady=2.5)
                return
        else:
            Label(self.enviar, text="Agregar asunto y mensaje.", fg='red').grid(row=4, column=0, columnspan=2, pady=2.5)
            self.asunto_e.focus()

if __name__ == "__main__":
    app = Tk()
    aplicacion = Tienda(app)
    app.mainloop()
