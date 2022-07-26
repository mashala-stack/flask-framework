from flask import Flask,session
from flask_session import Session

sess= Session()
def create_app():
    app = Flask(__name__,instance_relative_config=False)

    from .models import db
    DATABASE_PATH = 'sqlite:///myDb.db'
    # DATABASE_PATH = 'mysql+pymysql://root@localhost:3306/database'
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_PATH
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = "sdkjajkds83w942hnajsdhnbasdja"


    db.init_app(app)
    sess.init_app(app)


    
    with app.app_context():
        from .myApp import myApp

        app.register_blueprint(myApp.app_bp)

        db.create_all()

    return app