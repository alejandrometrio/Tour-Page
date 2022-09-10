from flask import Flask

app = Flask(__name__)

#Generar la secret_key
app.secret_key = "Esta es mi llave super secreta"

app.config['UPLOAD_FOLDER']= 'flask_app/static/img/'

