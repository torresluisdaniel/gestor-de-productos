# **Gestor de productos**

#### **Python 3.8**

```
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import smtplib
import sqlite3
```

Es un programa desarrollado en python, con ayuda de la libreria Tkinter.

## **Funciones**

- Agregar productos
- Ver productos
- Editar productos
- Eliminar productos
- Soporte

Programa enfocado a mantener un orden en el inventario, con un acceso con el fin habilitar todas las funciones, donde el usuario y contraseña están dados como.

- Usuario: **admin**
- Contraseña: **1234**

Le proporcionará **acceso** a la base de datos donde esta se almacenan los datos guardados, el usuario y contraseña, pueden ser cambiado en la siguiente sección de codigo.

**51**

```
   def entrar(self):

        user = str(self.usuario_e.get())
        clave = str(self.clave_e.get())

        if self.validar():

            if (user == "admin" and clave == "1234"):
```

---

Solo tres parametros del productos o objetos seran guardados en la base de datos de la siguiente manera; nombre, cantidad, precio, el nombre de las columnas podran ser cambiados en la siguiente sección de codigo.

**123**

```
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
```

EL parameto **columns** asigna el numero de columnas que se montrarán, despues agrega el titulo de cada columna con, **heading**, posterior a eso dara errores en gran parte de programa debido que debe agregar en las funciones necesarias del codigo la nueva columna, como.

**143 - 196**

```
    def agregar(self):

    def editar(self):
```

Tambien puede administar tu base de datos con el siguiente programa gratuito y funcional en todas las plataformas.

**[DB Browser for SQLite](https://sqlitebrowser.org/)**

---

Para obtener la funconalidad de soporte, primero debe editar el programa en las siguiente linea.

**318**

```
    smtpserver.login('correo_e', 'contraseña_e')

    subject = str(self.asunto_e.get())
    mensanje = str(self.text_e.get())

    mensanje = 'Subject: {}\n\n{}'.format(subject, mensanje)

    smtpserver.sendmail('correo_e', 'enviar_a', mensanje)
```

Donde **correo_e** y **contraseña_e** deben ser el correo el cual va a enviar el mensaje a **enviar_a**, se requiere la contraseña para iniciar sesión en **gmail**, (no funcionan con **hotmail**.) se puede cambiar directamente, o sea reemplazar **correo_e** por el correo a iniciar sesión, **correo@gmail.com** o otra opción es crear las variables dentro de la función, con la siguiente sintaxis.

```
correo_e = ("correo@gamil.com")
contraseña_e = ("contraseña")
enviar_a = ("enviar@gmail.com")
```

Posterior a eso, debe activar los inicios de sesión pocos seguros del correo que enviar el mensaje o sea, **correo_e**, en el siguiente link podra activalo.

**[Inicios - Google](https://myaccount.google.com/lesssecureapps)**

Debe asegurarse que la cuenta en la que va activar la opción sea la correcta, recomiento hacerlo en una ventana de incógnito.

> Nota: Si presenta error con los archivos como iconos o la base de datos cambie la ruta de los archivos, cambiar **_".\src\ico\logo.ico"_** a **_".\ico\logo.ico_"** lo mismo para todos los archivos, ubicados en, **15, 22, 149, 209, 288.**

---

<p style="font-size: 10px;">Todos los derechos a <a href="https://www.instagram.com/luisdanieltorresacosta/" target="_blank">Luis Daniel Torres.</a></p>

<p style="font-size: 10px;">Versión - 1.0</p>
