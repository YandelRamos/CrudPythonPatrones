from flask import Flask, render_template, request, redirect
from controllers.user_controller import UserController

app = Flask(__name__)
controller = UserController()

@app.route("/")
def index():
    users = controller.listar_usuarios()
    return render_template("index.html", users=users)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    email = request.form["email"]
    controller.agregar_usuario(name, email)
    return redirect("/")

@app.route("/edit/<int:id>")
def edit(id):
    users = controller.listar_usuarios()
    user = next((u for u in users if u[0] == id), None)
    return render_template("edit.html", user=user)

@app.route("/edit/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    email = request.form["email"]
    controller.editar_usuario(id, name, email)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    controller.eliminar_usuario(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)