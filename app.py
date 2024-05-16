from flask import Flask, render_template, request, redirect, url_for
from classes.Utilizador import Utilizador as Person
from classes.userlogin import Userlogin
from classes.reserva import Reserva
from classes.ementa import Ementa

app = Flask(__name__)
path = 'data/cantina.db'
Person.read(path)
prev_option = ""  
Ementa.read(path) 
Userlogin.read(path) 
Reserva.read(path)
#userlogin.read(filename=)

 #@app.route("/", methods=["post","get"])
 #def index():
     #global prev_option
     #butshow = "enabled"
     #butedit = "disabled"
     #option = request.args.get("option")
     #if option == "edit":
       #  butshow = "disabled"
        # butedit = "enabled"
     #elif option == "delete":
      #   obj = Person.current()
       #  Person.remove(obj.code)
        # if not Person.previous():
         #    Person.first()
         #Person.write(path)
     #elif option == "insert":
      #   butshow = "disabled"
       #  butedit = "enabled"
     #elif option == 'cancel':
      #   pass
     #elif prev_option == 'insert' and option == 'save':
         #strobj = request.form["code"] + ';' + request.form["name"] + ';' + \
         #request.form["dob"] + ';' + request.form["salary"]
         #Person.from_string(strobj)
         #Person.write(path)
         #Person.last()
     #elif prev_option == 'edit' and option == 'save':
         #obj = Person.current()
         #obj.code = request.form["code"]
         #obj.name = request.form["name"]
         #obj.dob = request.form["dob"]
         #obj.salary = float(request.form["salary"])
         #Person.write(path)
     #elif option == "first":
         #Person.first()
     #elif option == "previous":
         #Person.previous()
     #elif option == "next":
         #Person.nextrec()
     #elif option == "last":
         #Person.last()
     #elif option == 'exit':
         #return "<h1>Thank you for using Person app</h1>"
     #prev_option = option
     #obj = Person.current()
     #if option == 'insert':
     #    code,name,dob,salary = "","","",""
     #else:
      #   code = obj.code
      #   name = obj.name
      #   dob = obj.dob
      #   salary = obj.salary

      #return render_template("index.html", butshow=butshow, butedit=butedit)#,\
                                #code=code,name=name,dob=dob,salary=salary)
 #if __name__ == '__main__':
  #   app.run() 
  
  
  
  
  
  
  


 
Userlogin("user1", "admin", Userlogin.set_password("password1"))
Userlogin("user2", "user", Userlogin.set_password("password2"))

@app.route("/", methods=["POST", "GET"])
def login():
     if request.method == "POST":
         username = request.form["username"]
         password = request.form["password"]
         message=Userlogin.chk_password(username, password)
         if message == "Valid":
            
             return render_template("success.html", username=username)
         else:
             
             return render_template("error.html", message=message)
     else:
         
         return render_template("login.html") 

@app.route("/success/<username>")
def success(username):
     return render_template("success.html", username=username) 
@app.route("/login", methods=["GET"])
def return_to_login():
     return redirect(url_for("login"))


@app.route("/menu/<username>")
def menu(username):
    
    user = Person.get_by_username(username)

    
    reservas = Reserva.get_by_username(username)

    
    return render_template("menu.html", user=user, reservas=reservas)

@app.route("/reservar/<username>", methods=["GET", "POST"])
def reservar(username):
    if request.method == "POST":
        
        data = request.form["data"]
        prato = request.form["prato"]

       
        #codigo_reserva = generate_reservation_code()

        
        #reserva = Reserva(data, prato, codigo_reserva)

        
        #reserva.save()

        
        return redirect(url_for("menu", username=username))
    else:
       
        ementas = Ementa.get_all()

        
        return render_template("reservar.html", username=username, ementas=ementas)






if __name__ == "__main__":
     app.run(debug=True)
 
 
 
 
 
 
 
 
 
 