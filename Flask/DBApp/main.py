from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#DB Config.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db=SQLAlchemy(app)

#Model(Table) Creation
class Studinfo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    city=db.Column(db.String(20))
    email=db.Column(db.String(100))
    

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        nm=request.form["name"]
        ct=request.form['city']
        em=request.form['email']
        
        st=Studinfo(name=nm,city=ct,email=em)
        db.session.add(st)
        db.session.commit() #save
        print("Record Inserted!")
        return redirect('/')
    else:
        print("Error!")
    return render_template('index.html')

@app.route('/showdata',methods=['GET'])
def showdata():
    stdata=Studinfo.query.all()
    return render_template('showdata.html',stdata=stdata)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)