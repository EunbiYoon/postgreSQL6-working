from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:Ella135!@localhost/quotes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # event notification - track resources
app.debug=True

db = SQLAlchemy(app)


class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
	return redirect(url_for('index'))
