from flask import Flask

UPLOAD_FOLDER = 'C:/Users/Adhikari/Desktop/Hackday-master/upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
