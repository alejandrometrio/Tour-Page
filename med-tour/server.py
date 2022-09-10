from flask_app import app

#Importando Controlador
from flask_app.controllers import tour_controller, users_controller
from flask_app.models import users



if __name__=="__main__":
    app.run(debug=True)