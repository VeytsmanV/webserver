from db import DB
from flask import Flask, redirect, render_template, session
from login_form import LoginForm
from policeman_model import PolicemanModel
from criminal_model import CriminalsModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db = DB()
criminalsModel(db.get_connection()).init_table()
UsersModel(db.get_connection()).init_table()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_model = UsersModel(db.get_connection())
        exists = user_model.exists(user_name, password)
        if (exists[0]):
            session['username'] = user_name
            session['user_id'] = exists[1]
        return redirect("/index")
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
def logout():
    session.pop('username', 0)
    session.pop('user_id', 0)
    return redirect('/login')


@app.route('/')
@app.route('/index')
def index():
    if 'username' not in session:
        return redirect('/login')
    criminals = criminalsModel(db.get_connection()).get_all(session['user_id'])
    return render_template('index.html', username=session['username'], criminals=criminals)


@app.route('/add_criminals', methods=['GET', 'POST'])
def add_criminals():
    if 'username' not in session:
        return redirect('/login')
    form = AddcriminalsForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        nm = CriminalsModel(db.get_connection())
        nm.insert(title, content, session['policeman_id'])
        return redirect("/index")
    return render_template('add_criminals.html', title='Новый разыскиваемый', form=form, policeman=session['полицейский'])


@app.route('/delete_criminals/<int:criminals_id>', methods=['GET'])
def delete_criminals(criminals_id):
    if 'username' not in session:
        return redirect('/login')
    nm = criminalsModel(db.get_connection())
    nm.delete(criminals_id)
    return redirect("/index")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)