from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from classes.Utilizador import Utilizador as Person
from classes.userlogin import Userlogin
from classes.reserva import Reserva
from classes.ementa import Ementa
from classes.prato import Prato


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
    
    assigned_dishes = {"carne": [], "peixe": [], "vegetariano": []}
    
    for cod in menu_data:
        prato = Prato.obj[cod]
        for day in menu_sorted:
            if menu_sorted[day][prato.tipo] is None and prato.cod not in assigned_dishes[prato.tipo]:
                menu_sorted[day][prato.tipo] = prato
                assigned_dishes[prato.tipo].append(prato.cod)
                break

    return menu_sorted

def remember_user(username, password):
    resp = make_response(redirect(url_for('index', username=username)))  
    resp.set_cookie('username', username, max_age=6060247)  
    resp.set_cookie('password', password, max_age=6060247)
    return resp

def get_remembered_user():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    return username, password

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        message = Userlogin.chk_password(username, password)
        if message == "Valid":
            user = Userlogin.obj[username]
            session["username"] = username
            session["usergroup"] = user._usergroup
            
            if "remember_me" in request.form:  
                response = remember_user(username, password)
                return response  
                
            return render_template("index.html", username=username, group=session["usergroup"])
        else:
            return render_template("error.html", message=message)
    else:
       
        remembered_username, remembered_password = get_remembered_user()
        if remembered_username and remembered_password:
           
            message = Userlogin.chk_password(remembered_username, remembered_password)
            if message == "Valid":
                user = Userlogin.obj[remembered_username]
                session["username"] = remembered_username
                session["usergroup"] = user._usergroup
                return render_template("index.html", username=remembered_username, group=session["usergroup"])
        
        return render_template("login.html") 


@app.route('/logoff')
def logoff():
    session.clear()
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('username', '', expires=0)  
    resp.set_cookie('password', '', expires=0)
    return resp


@app.route("/Cantina/<username>")
def index(username):
    return render_template("index.html", username=username, group=session.get("usergroup"))


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



@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        senha = request.form["senha"]
        email = request.form["email"]
        role = 'cliente'
        codigo = str(Person.procuraNovoCodigo() + 1)
        s = f'{codigo};{name};{role};{senha};{email}'
        f = f'{email};{role};{senha}'
        
        Person.from_string(s)
        Person.insert(codigo)
        
        Userlogin.from_string(f)
        Userlogin.insert(email)   
        
        return redirect(url_for("login"))
    else:
        return render_template("signup.html")




@app.route("/relatorio/<username>")
def relatorio(username):
    if session.get("usergroup") != "funcionário":
        return redirect(url_for("index", username=username))

    total_reservations = len(Reserva.lst)
    carne_reservations = len([r for r in Reserva.lst if Reserva.obj[r]._tipo == "Carne"])
    peixe_reservations = len([r for r in Reserva.lst if Reserva.obj[r]._tipo == "Peixe"])
    vegetariano_reservations = len([r for r in Reserva.lst if Reserva.obj[r]._tipo == "Vegetariano"])

    if session.get("usergroup") != "funcionário":
        return redirect(url_for("index", username=username))

    # Calculate the number of reserved dishes by type
    total_reservations = len(Reserva.lst)
    carne_reservations = len([r for r in Reserva.lst if Reserva.obj[r]._tipo == "Carne"])
    peixe_reservations = len([r for r in Reserva.lst if Reserva.obj[r]._tipo == "Peixe"])
    vegetariano_reservations = len([r for r in Reserva.lst if Reserva.obj[r]._tipo == "Vegetariano"])

    return render_template("relatorio.html", username=username, total_reservations=total_reservations,
                           carne_reservations=carne_reservations, peixe_reservations=peixe_reservations,
                           vegetariano_reservations=vegetariano_reservations)


if __name__ == "__main__":
    app.run(debug=True)
