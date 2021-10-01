from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail
from waitress import serve

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)
mail = Mail(app)
db.init_app(app)
migrate.init_app(app, db)
login.init_app(app)
moment.init_app(app)


if __name__ == "__main__":
    # app.run(ssl_context=('cert.pem', 'key.pem'))
    serve(app, host='0.0.0.0', port=5000, url_scheme='https')


from app import routes, models 