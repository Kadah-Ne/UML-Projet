#install flask while being in active VENV:  pip install flask

from flask import Flask, session, redirect, url_for, escape, request ,render_template
app = Flask(__name__)

# @app.route('/login',methods=['GET','POST'])
# def Login():
#    return render_template('login.html')

@app.route('/', methods=['GET','POST'])
def index():
   if request.method == "POST":
      if request.form['idTxt'] == "Martin" and request.form['pwdTxt'] == '1':
         return render_template('index.html')
      else :
         return render_template('login.html')
if __name__ == '__main__':
   app.run()