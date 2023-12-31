from flask import Flask,render_template,redirect,request,url_for
from models import *

# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postgres'  # Remplacez database.db par le nom de votre base de données
# db = SQLAlchemy(app)

# class User(db.Model): 
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
        
#     def get_user(user_id):
#         user = User.query.get(user_id)
#         return user

# @app.route('/users')
# def users():
#     # all_users = User.query.all()
#     all_user=User.get_user(11)
#     return render_template('users.html', all_users=all_users)

app= Flask(__name__)
data = None
@app.route('/')
def home():
    global data
    return render_template("base.html")

# INSCRIPTION
@app.route('/signin',methods=['GET','POST'])
def signin():
    global data
    if request.method=='POST':
        addUser(email=request.form["email"],login=request.form["username"],mdp=request.form["password"])
        # Handle POST Request here
        # return redirect(url_for('login'))
        return "<h1>COMPTE CREE AVEC SUCCES</h1> <a href='/login'><h1>Se connecter</h1></a> <a href='/'><h1>Acceuil</h1></a>"
        
    return render_template("signin.html")

# CONNEXION
@app.route('/login',methods=['GET','POST'])
def login():
    global data
    if request.method=='POST':
        info=VerifUser(login1=request.form["username"],mdp=request.form["password"])
        # Handle POST Request here
        if info:
            data=info
            allUserTasks=readTasks(data[0])
            return render_template('taches.html',data=data,data2=allUserTasks)
        else:
          return "<h1>MOT DE PASSE OU USERNAME INCORRECT</h1> <a href='/login'><h1>Reessayer</h1></a>"
    else:
        return render_template("login.html")
    
    
# PAGE USER
@app.route('/taches/<int:idUser>',methods=['GET','POST'])
def taches(idUser):
    global data
    print(idUser)
    data2=readTasks(idUser)
    return render_template('taches.html',data2=data2,data=data)



# AJOUT
@app.route('/addtask/<int:idUser>',methods=['GET','POST'])
def addtask(idUser):
    global data
    if request.method=='POST':
        print(idUser)
        addTask(idUser,titre=request.form['title'],description=request.form['description'],date=request.form['datexp'])
        data2=readTasks(idUser)
        return render_template('taches.html',data2=data2,data=data)
    return render_template('addtask.html',data=data)
    # return render_template('addtask.html')
    
    
# MODIFICATION 
@app.route('/edit/<int:idUser>/<int:idTache>',methods=['GET','POST'])
def edittask(idUser,idTache):
    global data
    # recuperer les infos de la tache en question
    infotache=readTask(idTache,idUser)
    print(infotache)
    if request.method=='POST':
        modifyTask(idTache,request.form['title'],request.form['description'],request.form['datexp'])
        # recuperer a nouveau les taches de l'utilisateur
        data2=readTasks(idUser)
        return render_template('taches.html',data2=data2,data=data)
        
    # modifier la tache
    
    return render_template('edit.html',infotache=infotache)

# SUPRESSION
@app.route('/delete/<int:idUser>/<int:idTache>',methods=['GET','POST'])
def deletetask(idUser,idTache):
    global data
    deleteTask(idTache,idUser)
    # recuperer a nouveau les taches de l'utilisateur
    data2=readTasks(idUser)
    return render_template('taches.html',data2=data2,data=data)
    







