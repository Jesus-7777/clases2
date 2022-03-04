from fileinput import close
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

#TODO: conectar a la base de datos

db = mysql.connector.connect(
host ='localhost',
password='', 
user='root',
database="pro_crud",
port=3306

)
db.autocommit=True #TODO: esta linea es para que la base de datos no guarde la cahe
"""Instancia de la variable name"""

app = Flask(__name__) 

"""Funcion decoradora(herencia)"""
@app.get("/")
def index():
    #TODO:ponemos abrimos una variable cursor para conectar a la base de datos
   #el dictionario se pone para que la informacion sea legible y poder entenderla, se pone solo para consultar datos
    
    cursor=db.cursor(dictionary=True)
    
    #TODO:esto resive solo una cadena de texto, se manda cualquier consulta SQL
    cursor.execute('select * from productos')
    
    productos= cursor.fetchall()
    #TODO:productos= cursor.fetchone()-nos muestra un producto
    
    #TODO:print(productos[1]['nombre']) 
    
    #TODO:luego cerramos el cursor para que no se quede abirta la base de datos
    cursor= close()
    return render_template("index.html",productos=productos)


#TODO: fromulario para crear producto
@app.get("/crear")
def crearProducto():
    return render_template("crear.html")


#TODO: metodo para enviar el formulario a la base de datos
@app.post("/crear")
def crearProductoPost():
    nombre=request.form.get('nombre')
    precio=request.form.get('precio')
    cursor=db.cursor()
    cursor.execute("insert into productos(nombre, precio) values(%s,%s)",(nombre,precio,))
    cursor.close()
    
    return redirect(url_for('index'))   

 #TODO: pagina de contactos
@app.get("/contacto")
def contacto():
    return render_template("/contactos/index.html")

#TODO: pagina para editar el id de l contacto
@app.get("/contacto/<contactoId>/edit")
def editarContacto(contactoId):
    
    suma = 2+2
    return render_template("contactos/editar.html", contactoId = contactoId, suma = suma)
    
    #http://localhost:5000/contacto/6/edit

#TODO: calcular año de nacimiento
@app.get("/contacto/<int:nacimientoId>/edad/")
def ediEdad(nacimientoId):
    
   resta = 2022 - nacimientoId
   return render_template("contactos/edad.html",resta=resta)
    
app.run(debug=True)

