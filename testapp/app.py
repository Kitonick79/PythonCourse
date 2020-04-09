from flask import Flask
from .database import init_db
from .common import views as common_views
from .users import views as user_views

app = Flask(__name__)
app.config.from_object('testapp.settings')
init_db(app)
app.register_blueprint(common_views.app)
app.register_blueprint(user_views.app)
