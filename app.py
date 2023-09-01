from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, update
from datetime import datetime
from flask import Flask, render_template, request, send_from_directory, url_for, redirect
import os 

app = Flask(__name__)

username =' '
"""app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), nullable=True)
    content = db.Column(db.String(700), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    
    
class Wb_entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_number=db.Column(db.Integer)
    user = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(), nullable=True)
    edited_last = db.Column(db.DateTime(), default=datetime.utcnow)

"""



@app.route('/')
def login():
    return render_template('login.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('login'))
   
"""@app.route('/index', methods=['POST'])
def start_page():
    name = request.form.get('name')
    global username 
    username = name 
    if name:
        return render_template('index.html', name = username)
    else:
       return redirect(url_for('login'))
    
 
@app.route("/chat", methods=["GET", "POST"])
def start_chat():
    if request.method == "POST":
        new_message = Message(
            user = username,
            content = request.form["content"]
            ) 
        db.session.add(new_message)
        db.session.commit()
    messages = Message.query.order_by(Message.created_at.desc()).all()
    return render_template("chat.html", messages=messages, name=username)




@app.route("/Worldbuilding", methods=("GET", "POST"))
def start_worldbuilding():
    for i in range (1,4):
        if db.session.query(db.exists().where(Wb_entry.entry_number == i and Wb_entry.user == username)).scalar() == False:
            new_entry = Wb_entry(
                user = username,
                content = "Beispiel",
                entry_number = i
                ) 
            db.session.add(new_entry)
            db.session.commit()
            
    if request.method == "POST":    
        for i in range (1,4):
            if db.session.query(db.exists().where(Wb_entry.entry_number == i and Wb_entry.user == username)).scalar() == True:
                user = Wb_entry.query.filter_by(user = username, entry_number = i).one()
                db.session.delete(user)
                db.session.commit()
                
            Textfield = "text_" + str(i)
            
            new_entry = Wb_entry(
            user = username,
            content = request.form[Textfield],
            entry_number = i
            ) 
            db.session.add(new_entry)
            db.session.commit()
            
    content_1 = Wb_entry.query.filter_by(entry_number = 1, user = username)
    content_2 = Wb_entry.query.filter_by(entry_number = 2, user = username)
    content_3 = Wb_entry.query.filter_by(entry_number = 3, user = username)
    
    return render_template("worldbuild.html", content_1 = content_1, content_2 = content_2, content_3 = content_3)
   """
"""user = Wb_entry.query.filter_by(user="Paul").one()
    db.session.delete(user)
    db.session.commit()""" 
  
  
"""
@app.route("/characterBuilder")
def start_Character():
        return render_template("Character.html", name = username)

"""
if __name__ == '__main__':
    app.run()


