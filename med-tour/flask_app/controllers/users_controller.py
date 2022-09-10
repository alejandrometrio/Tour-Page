from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app

#Importando el Modelo de User
from flask_app.models.users import User

#Importamos el modelo de Recetas
from flask_app.models.tour import Tour
from werkzeug.utils import secure_filename
import os


#Importando BCrypt (encriptar)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) #inicializando instancia de Bcrypt

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/createaccount')
def createaccount():
    return render_template('index2.html')

@app.route('/register', methods=['POST'])
def register():

    if not User.valida_usuario(request.form):
        return redirect('/')

    pwd = bcrypt.generate_password_hash(request.form['password'])

    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "nationality": request.form['nationality'],
        "email": request.form['email'],
        "password": pwd
    }

    id = User.save(formulario) 

    session['usuario_id'] = id 

    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("E-mail not found", 'login')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Wrong Password ", 'login')
        return redirect('/')
    
    session['usuario_id'] = user.id

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario) 

    tour = Tour.get_all() 

    return render_template('dashboard.html', user=user, tour=tour)



@app.route('/edit/user/<int:id>') 
def edit_user(id):
    if 'usuario_id' not in session:  
        return redirect('/')
    
    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario) 

    formulario_tours = { "id": id }
    mtours = Tour.get_user_places(formulario_tours)

    return render_template('edit_user.html', user=user, thetours=mtours )



@app.route('/update/user', methods=['POST'])
def update_user():
    if 'usuario_id' not in session: 
        return redirect('/')
    
    # if not User.valida_usuario2(request.form):
    #     return redirect('/edit/user/'+request.form['id'] )

    User.update(request.form)

    return redirect('/dashboard')



@app.route('/game')
def jugar():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear() 
    return redirect('/') 
