from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Very_secret'

from cap import routes
