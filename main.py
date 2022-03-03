from flask import Flask, render_template, template_rendered

"""Instancia de la variable name"""
app = Flask(__name__) 

"""Funcion decoradora(herencia)"""
@app.get("/")
def index():
    return render_template("index.html")

@app.get("/contacto")
def contacto():
    return render_template("/contactos/index.html")
@app.get("/contacto/<contactoId>/edit")
def editarContacto(contactoId):
    
    suma = 2+2
    return render_template("contactos/editar.html", contactoId = contactoId, suma = suma)
    
    #http://localhost:5000/contacto/6/edit

@app.get("/contacto/<int:nacimientoId>/edad/")
def ediEdad(nacimientoId):
    
   resta = 2022 - nacimientoId
   return render_template("contactos/edad.html",resta=resta)
    
app.run(debug=True)

