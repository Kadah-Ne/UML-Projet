#install flask while being in active VENV:  pip install flask
import DBmanager
from flask import Flask, session, redirect, url_for, escape, request ,render_template, make_response
app = Flask(__name__)

# @app.route('/login',methods=['GET','POST'])
# def Login():
#    return render_template('login.html')

@app.route('/', methods=['GET','POST'])
def index():
   if request.method == "POST":
      if request.form['idTxt'] == "Martin" and request.form['pwdTxt'] == '1':
         session["idTxt"] = request.form['idTxt']
         session["isLib"] = True
         return render_template("index.html")
      else :
         return render_template('login.html')
   else :
      return render_template('login.html')

@app.route('/catalog', methods=['GET','POST'])
def catalog():
   data = tuple(DBmanager.characterlist()) # format in ((info))
   heading = ("ISBN", "name", "overview", "publisher", "publicationDate", "lang")
   if request.method == "POST":
      session["Library"] = request.form["Library"]
      return render_template("playerstable.html", headings=heading, data=data,user = session.get("idTxt"),library = session.get("Library")) #render_template te permet d'executer un HTML(doit etre dans dossier template)

if __name__ == '__main__':
   app.secret_key ="2ifnidkohéijfhizdhnazfnaz,faznfç(jicno)"
   app.run()
   

