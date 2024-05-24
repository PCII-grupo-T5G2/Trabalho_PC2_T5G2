from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from classes.Utilizador import Utilizador as Person
from classes.userlogin import Userlogin
from classes.reserva import Reserva
from classes.ementa import Ementa
from classes.prato import Prato
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

app = Flask(__name__)
path = 'data/cantina.db'
Person.read(path)
Ementa.read(path)
Userlogin.read(path)
Reserva.read(path)
Prato.read(path)
app.secret_key = 'BAD_SECRET_KEY'

Userlogin("user1", "admin", Userlogin.set_password("password1"))
Userlogin("user2", "user", Userlogin.set_password("password2"))

def get_menu_for_week(week):
    Prato.set_filter({"_semana": [str(week)]})
    menu_data = Prato.lst
    menu_sorted = {"Segunda": {"carne": None, "peixe": None, "vegetariano": None},
                   "Terça": {"carne": None, "peixe": None, "vegetariano": None},
                   "Quarta": {"carne": None, "peixe": None, "vegetariano": None},
                   "Quinta": {"carne": None, "peixe": None, "vegetariano": None},
                   "Sexta": {"carne": None, "peixe": None, "vegetariano": None}}
    for cod in menu_data:
        prato = Prato.obj[cod]
        if prato.tipo == "carne":
            menu_sorted["Segunda"]["carne"] = prato if menu_sorted["Segunda"]["carne"] is None else menu_sorted["Segunda"]["carne"]
            menu_sorted["Terça"]["carne"] = prato if menu_sorted["Terça"]["carne"] is None else menu_sorted["Terça"]["carne"]
            menu_sorted["Quarta"]["carne"] = prato if menu_sorted["Quarta"]["carne"] is None else menu_sorted["Quarta"]["carne"]
            menu_sorted["Quinta"]["carne"] = prato if menu_sorted["Quinta"]["carne"] is None else menu_sorted["Quinta"]["carne"]
            menu_sorted["Sexta"]["carne"] = prato if menu_sorted["Sexta"]["carne"] is None else menu_sorted["Sexta"]["carne"]
        elif prato.tipo == "peixe":
            menu_sorted["Segunda"]["peixe"] = prato if menu_sorted["Segunda"]["peixe"] is None else menu_sorted["Segunda"]["peixe"]
            menu_sorted["Terça"]["peixe"] = prato if menu_sorted["Terça"]["peixe"] is None else menu_sorted["Terça"]["peixe"]
            menu_sorted["Quarta"]["peixe"] = prato if menu_sorted["Quarta"]["peixe"] is None else menu_sorted["Quarta"]["peixe"]
            menu_sorted["Quinta"]["peixe"] = prato if menu_sorted["Quinta"]["peixe"] is None else menu_sorted["Quinta"]["peixe"]
            menu_sorted["Sexta"]["peixe"] = prato if menu_sorted["Sexta"]["peixe"] is None else menu_sorted["Sexta"]["peixe"]
        elif prato.tipo == "vegetariano":
            menu_sorted["Segunda"]["vegetariano"] = prato if menu_sorted["Segunda"]["vegetariano"] is None else menu_sorted["Segunda"]["vegetariano"]
            menu_sorted["Terça"]["vegetariano"] = prato if menu_sorted["Terça"]["vegetariano"] is None else menu_sorted["Terça"]["vegetariano"]
            menu_sorted["Quarta"]["vegetariano"] = prato if menu_sorted["Quarta"]["vegetariano"] is None else menu_sorted["Quarta"]["vegetariano"]
            menu_sorted["Quinta"]["vegetariano"] = prato if menu_sorted["Quinta"]["vegetariano"] is None else menu_sorted["Quinta"]["vegetariano"]
            menu_sorted["Sexta"]["vegetariano"] = prato if menu_sorted["Sexta"]["vegetariano"] is None else menu_sorted["Sexta"]["vegetariano"]
    return menu_sorted



@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        message = Userlogin.chk_password(username, password)
        if message == "Valid":
            session["username"] = username
            session["usergroup"] = "user"  # Assuming user group is retrieved from the login info
            return render_template("index.html", username=username, group=session["usergroup"])
        else:
            return render_template("error.html", message=message)
    else:
        return render_template("login.html")

@app.route("/Cantina/<username>")
def index(username):
    return render_template("index.html", username=username)

@app.route("/login", methods=["GET"])
def return_to_login():
    return redirect(url_for("login"))

@app.route("/menu/<username>", methods=["GET", "POST"])
def menu(username):
    if request.method == "POST":
        week = request.form["week"]
        menu_data = get_menu_for_week(week)
        return render_template("menu.html", username=username, menu=menu_data, week=week)
    else:
        week = request.args.get('week', default=1, type=int)
        menu_data = get_menu_for_week(week)
        return render_template("menu.html", username=username, menu=menu_data, week=week)

@app.route("/reservar/<username>", methods=["POST", "GET"])
def reservar(username):
    if request.method == "POST":
        data_str = request.form["Data"]
        refeicao = request.form["Refeição"]
        tipo = request.form["Tipo"]
        
        if data_str != "":
            data = datetime.strptime(data_str, "%Y-%m-%d").date()
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime('%Y-%m-%d')
            new_datetime = datetime.strptime(formatted_datetime, '%Y-%m-%d').date()
            
            if refeicao in ["Almoço", "Jantar"] and data > new_datetime:
                codigo = str(Reserva.procuraNovoCodigo() + 1)
                s = f'{codigo};{data_str};{refeicao};{tipo};{username}'
                Reserva.from_string(s)
                Reserva.insert(codigo)
                return redirect(url_for("success", username=username))
            else:
                return redirect(url_for("reservas_invalidas", username=username))
        else:
            return redirect(url_for("reservas_invalidas", username=username))
    else:
        return render_template("reservar.html", username=username)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/reservas_invalidas/<username>")
def reservas_invalidas(username):
    return render_template("reservas_invalidas.html", username=username)

@app.route("/reservas/<username>")
def reservas(username):
    user_reservations = Reserva.get_reservations_by_user(username)
    return render_template("reservas.html", username=username, reservations=user_reservations)

def remember_user(username, password):
    resp = make_response()
    resp.set_cookie('username', username, max_age=6060247)  # 1 week expiration
    resp.set_cookie('password', password, max_age=6060247)
    return resp

def get_remembered_user():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    return username, password

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        senha = request.form["senha"]
        email = request.form["email"]
        role = 'cliente'
        codigo = str(Person.procuraNovoCodigo() + 1)
        s = f'{codigo};{name};{role};{senha};{email}'
        f = f'{email};{role};{name}'
        
        Person.from_string(s)
        Person.insert(codigo)
        
        Userlogin.from_string(f)
        Userlogin.insert(email)
        
        return render_template("login.html")
    else:
        return render_template("signup.html")

@app.route('/reset_password', methods=['POST'])
def reset_password():
    username = request.form['username']
    # Logic to send password reset email to the user's email address
    # (you would implement this logic)
    return redirect(url_for('login'))

def generate_password():
    length = 10
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def send_email(receiver_email, new_password):
    sender_email = "your_email@example.com"
    password = "your_email_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Password Reset"

    body = f"Your new password is: {new_password}"
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]
        new_password = generate_password()

        # Here you would typically update the user's password in your database
        # For demonstration purposes, let's just print the new password
        print("New Password:", new_password)

        # Send password reset email
        send_email(email, new_password)

        return "Password reset instructions sent to your email."
    else:
        return render_template("forgot_password.html")

@app.route('/logoff')
def logoff():
    # Clear the session data
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
