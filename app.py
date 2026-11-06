from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
# specify where the database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # /// is relative path, //// is absolute path
db = SQLAlchemy(app)    # database initialized from the settings in our app

# define the database structure
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(256), nullable=False) # nullable False because we don't want this blank
    meaning = db.Column(db.String(256), nullable=False)
    last_reviewed = db.Column(db.DateTime)
    times_remembered = db.Column(db.Integer)    # check how many times the word was remembered correctly when reviewed

    def __repr__(self):
        return '<Word %r>' % self.word

# to create a database, do db.create_all()

@app.route('/')
def index():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)