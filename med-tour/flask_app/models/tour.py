from pickle import TRUE
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Tour:

    def __init__(self, data):
        self.id = data['id']
        self.place_name = data['place_name']
        self.category = data['category']
        self.price_range = data['price_range']
        self.schedule = data['schedule']
        self.description = data['description']
        self.location = data['location']
        self.reference_place = data['reference_place']
        self.user_id=data['user_id']


        self.updated_at=data['updated_at']
        self.created_at=data['created_at']

        self.first_name = data['first_name']
        self.last_name = data['last_name']

    #Funcion que valida los datos 
    @staticmethod
    def valida_tour(formulario):
        es_valido = True
        
        if len(formulario['place_name']) < 4:
            flash("El nombre debe tener al menos 4 caracteres", "places")
            es_valido = False
                
        if len(formulario['schedule']) < 4:
            flash("El horario debe tener al menos 4 caracteres", "places")
            es_valido = False
        
        if len(formulario['reference_place']) < 4:
            flash("El lugar de referencia debe tener al menos 4 caracteres", "places")
            es_valido = False
        
        return es_valido 
    
    #Funcion para guardar 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO places (place_name,  category, price_range, schedule, location, description,reference_place,user_id) VALUES ( %(place_name)s, %(category)s, %(price_range)s,%(schedule)s,%(location)s,%(description)s,%(reference_place)s,%(user_id)s )"
        nuevoId = connectToMySQL('tour').query_db(query, data)
        return nuevoId

    ##ACA SERIA EL ORDER BY 
    @classmethod
    def get_all(cls):
        query = "SELECT places.*, first_name, last_name FROM places LEFT JOIN users ON users.id = places.user_id" 
        results = connectToMySQL('tour').query_db(query) 
        places = []
        for m in results:
            places.append(cls(m)) 
        return places

    #Me trae toda la info de las spp
    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT places.*, first_name, last_name FROM places LEFT JOIN users ON users.id = places.user_id WHERE places.id = %(id)s "
        result = connectToMySQL('tour').query_db(query, formulario) 
        m= cls(result[0]) 
        return m

    @classmethod
    def get_user_places(cls, formulario):
        query = "SELECT * FROM places LEFT JOIN users ON users.id = places.user_id WHERE users.id = %(id)s "
        results = connectToMySQL('tour').query_db(query, formulario)
        places= []
        for a in results:
            places.append(cls(a))
        return places

    #Elimina la info de la sp
    @classmethod
    def delete(cls, formulario): 
        query = "DELETE FROM places WHERE id = %(id)s"
        result = connectToMySQL('tour').query_db(query, formulario)
        return result

    #Agrega los like a la bd
    @classmethod
    def likes(cls, formulario): 
        query = "INSERT INTO likes (user_id, place_id) VALUES (%(user_id)s,%(place_id)s)"
        result = connectToMySQL('tour').query_db(query, formulario)
        return result

    #Cuenta los likes y "crea la nueva vble num_likes"
    @classmethod
    def contar_likes(cls, data):
        id={"id":data}
        query= "SELECT count(place_id) as num_likes from likes where place_id= %(id)s"
        result = connectToMySQL('tour').query_db(query, id)
        return result

    #Permite que el usuario de SOLO like una vez
    @classmethod
    def insert_like(cls, data): 
        query= "SELECT * FROM likes WHERE place_id = %(place_id)s && user_id= %(user_id)s"
        result= connectToMySQL('tour').query_db(query,data)
        if result: 
            return  flash("I'm sorry, you have already clicked like to this" ,'places')
        else : 
            cls.likes(data)
            return TRUE
