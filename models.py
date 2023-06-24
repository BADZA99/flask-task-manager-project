import psycopg2

def get_connexion():
    con=psycopg2.connect(
        database="flaskdb",
        password="passer",
        host="localhost",
        user="postgres"
    )
    cur=con.cursor()
    return con,cur


# def create_table():
#     con,cur =get_connexion()
#     requete ="CREATE TABLE IF NOT EXISTS utilisateur(idU SERIAL PRIMARY KEY,email VARCHAR(255),login VARCHAR(25),mdp VARCHAR(20))"
#     cur.execute(requete)
#     con.commit()
#     con.close()

# create_table()

# creer la table tache avec iduser comme cle etrangere provenant de utilisateur (idU) ainsi que titre,


## creer un Etudiant
def addUser(email,login,mdp):
    con,cur =get_connexion()
    requete ="INSERT INTO utilisateur(email,login,mdp) VALUES (%s,%s,%s)"
    cur.execute(requete,(email,login,mdp))
    con.commit()
    print("utilisateur ajoute avec success !!!")
    con.close()    



def VerifUser(login1,mdp):
    con,cur =get_connexion()
    requete ="SELECT * FROM utilisateur where mdp=%s and login=%s"
    cur.execute(requete,(mdp,login1))
    utilisateur = cur.fetchone()
    con.close() 
    return utilisateur
    
## pour les taches
def addTask(idUser,titre,description,date):
    con,cur =get_connexion()
    requete ="INSERT INTO tache(iduser,titre,datedeche,description) VALUES (%s,%s,%s,%s)"
    cur.execute(requete,(idUser,titre,date,description))
    con.commit()
    print("tache ajoute avec success !!!")
    con.close()    

def readTasks(idUser):
    con,cur =get_connexion()
    requete ="SELECT * FROM tache,utilisateur where idu=%s and iduser=idu ORDER BY datedeche ASC"
    cur.execute(requete,(idUser,))
    tache = cur.fetchall()
    con.close() 
    return tache

def readTask(id,idUser):
    con,cur =get_connexion()
    requete ="SELECT * FROM tache,utilisateur where idt=%s and idu=%s and idUser=idU"
    cur.execute(requete,(id,idUser,))
    tache = cur.fetchone()
    con.close()
    return tache
    
def modifyTask(id,titre,description,date):
    con,cur =get_connexion()
    requete ="UPDATE tache set titre=%s,description=%s,datedeche=%s where idT=%s"
    cur.execute(requete,(titre,description,date,id))
    con.commit()
    print("tache modifier avec success !!!")
    con.close()   

def deleteTask(id,idU):
    con,cur =get_connexion()
    requete ="DELETE FROM tache where idt=%s and iduser=%s"
    cur.execute(requete,(id,idU))
    con.commit()
    print("SUPPRESSION fait avec success !!!")
    con.close()   
