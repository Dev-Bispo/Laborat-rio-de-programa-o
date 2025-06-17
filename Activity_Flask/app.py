from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/result", methods= ["GET","POST"])
def application():
    nme = request.form["username"]
    num = request.form["phone number"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    return render_template("result.html", name=nme, cpf=cpf, email=email, number=num)
    


if __name__ == "__main__":
    app.run(debug=True)
 

