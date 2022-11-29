#install flask while being in active VENV:  pip install flask
import DBmanager
import SearchFunctions as test
from flask import Flask, session, redirect, url_for, escape, request ,render_template, make_response
app = Flask(__name__)

# @app.route('/login',methods=['GET','POST'])
# def Login():
#    return render_template('login.html')

@app.route('/', methods=['GET','POST'])
def index():
   if request.method == "POST":
      UserSearch = test.LogIn(request.form['idTxt'],request.form['pwdTxt'])
      if UserSearch != -1:
         session["userName"] = request.form['idTxt']
         print(session["userName"])
         session["idUser"] = UserSearch[0]
         session["libId"] = UserSearch[1]
         if UserSearch[2] == "Lib":
            session["isLib"] = True
         else:
            session["isLib"] = False
         
         return redirect("/search")
      else:
         return render_template('login.html')
   else :
      return render_template('login.html')


@app.route("/search",methods = ["GET","POST"])
def search():
   data = tuple(DBmanager.characterlist()) # format in ((info))
   heading = ("ISBN", "Titre", "Tag", "Sujet", "Editeur", "Date d'edition", "Langue", "Auteur")
   if request.method == "POST":
      bookTitle = request.form["searchTitle"]
      bookAuthor = request.form["searchAuthor"]
      bookTopic = request.form["searchTopic"]
      bookFormat = request.form["format"]
      if bookAuthor != "" or bookTitle != "" or bookTopic != "" or bookFormat !="":
         data = tuple(test.search(bookTitle, bookAuthor, bookTopic, bookFormat, session.get("libId") ))
         #print(data)
         return render_template("search.html",user = session.get("userName"), data = data, headings = heading, Title = bookTitle, Author = bookAuthor, Topic = bookTopic, Format = bookFormat) #render_template te permet d'executer un HTML(doit etre dans dossier template)
      else :
         return render_template("search.html",user = session.get("userName"), data = data, headings = heading)
   else :
      return render_template("search.html",user = session.get("userName"), data = data, headings = heading)

@app.route("/book",methods = ["GET","POST"])
def book():
   if request.method == "POST":
      bookToView = test.search(request.form["title"],library=session.get("libId"))
      BookISNB = bookToView[0][0]
      BookTitle = bookToView[0][1]
      BookTag = bookToView[0][2]
      BookRecap = bookToView[0][3]
      BookPub = bookToView[0][4]
      BookDOR = bookToView[0][5]
      BookLang = bookToView[0][6]
      BookAuthor = bookToView[0][7]
      return render_template("book.html", id = BookISNB, title = BookTitle, isLib = session.get("isLib"), tag = BookTag, recap = BookRecap, editeur = BookPub, dateSortie = BookDOR, langue = BookLang, auteur = BookAuthor)

if __name__ == '__main__':
   app.secret_key ="2ifnidkohéijfhizdhnazfnaz,faznfç(jicno)"
   app.run()
   

