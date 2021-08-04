from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",content ="esting")

@app.route("/habitaciones")
def habitacion():
    return render_template("Habitaciones.html",content ="esting")

@app.route("/usuario")
def precios():
    return render_template("Usuario.html",content ="esting")

if __name__ == "__main__":
    app.run(debug=True)