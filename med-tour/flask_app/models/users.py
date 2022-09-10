from flask_app.config.mysqlconnection import connectToMySQL

import re #Importamos expresiones regulares
#crear una expresión regular para verificar que tengamos el email con formato correcto
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash, request #mandar mensajes a la plantilla



class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.nationality = data['nationality']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users(first_name, last_name, age,nationality,email,password) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(nationality)s,%(email)s,%(password)s)"
        result = connectToMySQL('tour').query_db(query, formulario) #1 - Insert recibe id
        return result #result = Identificador del nuevo registro

    @staticmethod
    def valida_usuario(formulario):

        es_valido = True
        

        if len(formulario['first_name']) < 3:
            flash("Name must be at least 3 characters.", 'registro')
            es_valido = False
        
        if len(formulario['last_name']) < 3:
            flash("Last Name must be at least 3 characters.", 'registro')
            es_valido = False
            
        if len(formulario['age']) < 1:
            flash("Must write an age.", 'registro')
            es_valido = False

        if len(formulario['nationality']) <= 0:
            flash("Must choose a country of nationality.", 'registro')
            es_valido = False
            
        if not EMAIL_REGEX.match(formulario['email']): 
            flash('Invalid Email ', 'registro')
            es_valido = False

        if len(formulario['password']) < 8:
            flash("Password must be at least 8 characters.", 'registro')
            es_valido = False
        
        if formulario['password'] != formulario['confirm_password']:
            flash("Passwords doesn't match", 'registro')
            es_valido = False
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('tour').query_db(query, formulario)
        if len(results) >= 1:
            flash("Email has been registered", 'registro')
            es_valido = False

        return es_valido

    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('tour').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            
            user = cls(result[0]) 
            return user

    @classmethod
    def update(cls, formulario): 
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s,  age=%(age)s,  nationality=%(nationality)s,  email=%(email)s WHERE id = %(id)s"
        result1 = connectToMySQL('tour').query_db(query, formulario)
        return result1

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('tour').query_db(query, formulario) 
        user = cls(result[0])
        return user

    # @staticmethod
    # def valida_usuario2(formulario):

    #     es_valido = True
        
    #     if len(formulario['first_name']) < 3:
    #         flash('Nombre debe de tener al menos 3 caracteres', 'registro')
    #         es_valido = False
        
    #     if len(formulario['last_name']) < 3:
    #         flash('Apellido debe de tener al menos 3 caracteres', 'registro')
    #         es_valido = False
            
    #     if len(formulario['age']) < 1:
    #         flash("Must write an age.", 'registro')
    #         es_valido = False

    #     if len(formulario['nationality']) < 3:
    #         flash('Tu nacionalidad debe de tener al menos 3 caracteres', 'registro')
    #         es_valido = False

    #     return es_valido
