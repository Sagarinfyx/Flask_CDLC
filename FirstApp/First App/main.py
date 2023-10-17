from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name


@app.route('/add/<name>')
def add_name(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return f"Added {name} to the database."


@app.route('/all')
def list_names():
    users = User.query.all()
    names = [user.name for user in users]
    return render_template('list.html', names=names)


if __name__ == '__main__':
    app.run(debug=True)
