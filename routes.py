from flask import Flask,render_template,redirect,request,url_for
from models import *
app= Flask(__name__)
error=0
data = None
@app.route('/')
def home():
    global data
    return render_template("base.html")

@app.route('/signin',methods=['GET','POST'])
def signin():
    global data
    if request.method=='POST':
        addUser(email=request.form["email"],login1=request.form["username"],mdp=request.form["password"])
        # Handle POST Request here
        return redirect(url_for('login'))
    return render_template("signin.html")

@app.route('/login',methods=['GET','POST'])
def login():
    global data
    if request.method=='POST':
        info=VerifUser(login1=request.form["username"],mdp=request.form["password"])
        # Handle POST Request here
        if info:
            data=info[0]
            # userTask=readTasks(userId)
            # print(data)
            return render_template('taches.html',data=data)
            # return redirect(url_for('taches'))
            
        else:
            error=1
            return render_template('login.html',error=error)
      
          # return "<h1>MOT DE PASSE OU USERNAME INCORRECT</h1> <a href='/login'><h1>Retry</h1></a>"
    else:
        return render_template("login.html")


@app.route('/taches/<int:idUser>',methods=['GET','POST'])
def taches(idUser):
    global data
    data2=readTasks(idUser)
    return render_template('affiche.html',data2=data2,data=data)


@app.route('/addtask/<int:idUser>',methods=['GET','POST'])
def addtask(idUser):
    global data
    if request.method=='POST':
        print(idUser)
        addTask(idUser,titre=request.form['title'],description=request.form['description'],date=request.form['datexp'])
        data2=readTasks(idUser)
        print(data2[0])
        # Handle POST Request here
        # if data== True:
        return render_template('taches.html',data2=data2,data=data)

    return render_template('addtask.html',data=data)
    # return render_template('addtask.html')

@app.route('/edit')
def edittask():
    global data
    return render_template('edit.html')







