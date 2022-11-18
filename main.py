#install flask while being in active VENV:  pip install flask
import DBmanager,test
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
         return redirect("/search")
      else :
         return render_template('login.html')
   else :
      return render_template('login.html')


@app.route("/search",methods = ["GET","POST"])
def search():
   data = tuple(DBmanager.characterlist()) # format in ((info))
   heading = ("ISBN", "name", "overview", "publisher", "publicationDate", "lang")
   print(session.get("idTxt"))
   if request.method == "POST":
      bookTitle = request.form["searchTitle"]
      bookAuthor = request.form["searchAuthor"]
      bookTopic = request.form["searchTopic"]
      bookFormat = request.form["format"]
      if bookAuthor != "" or bookTitle != "" or bookTopic != "" or bookFormat !="":
         data = tuple(test.search(bookTitle, bookAuthor, bookTopic, bookFormat, 1 ))
         return render_template("search.html",user = session.get("idTxt"), data = data, headings = heading, Title = bookTitle, Author = bookAuthor, Topic = bookTopic, Format = bookFormat) #render_template te permet d'executer un HTML(doit etre dans dossier template)
      else :
         return render_template("search.html",user = session.get("idTxt"), data = data, headings = heading)
   else :
      return render_template("search.html",user = session.get("idTxt"), data = data, headings = heading)

@app.route("/book",methods = ["GET","POST"])
def book():
   if request.method == "POST":
      return render_template("book.html", id = request.form["idbook"], title = request.form["title"], isLib = session.get("isLib"))

if __name__ == '__main__':
   app.secret_key ="2ifnidkohéijfhizdhnazfnaz,faznfç(jicno)"
   app.run()
   

