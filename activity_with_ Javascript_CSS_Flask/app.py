from flask import Flask, render_template, redirect, request, session, url_for, flash

app = Flask(__name__)
app.secret_key = "gbs"
 
@app.route("/",  methods=["GET", "POST"])
def formulario():
    
        
    username = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    
    
    
    if "store" not in session:
        session["store"] = []
    
        session["store"].extend([username, email, password])

    
    if request.method == "POST":    
        if request.form.get("Cadastrar") == "enviar": 

            return redirect(url_for("page"))
        
        
            
    return render_template("formulario.html")

@app.route("/page")
def page():
    flash("Cadastro realizado!")
    

    return render_template("page.html")
