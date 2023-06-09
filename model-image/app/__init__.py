import os

from flask import Flask,request
from . import db
from . import model
from . import auth

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    """
    app.config.from_mapping(
        SECRET_KEY='dev', # SECRET KEYS IN PUBLISHED APPS IS STUPID; wiLL OS.GETNV
        DATABASE=os.path.join(app.instance_path, 'fyh-database.db'),
    )
    """

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # registering blueprint
    app.register_blueprint(model.bp)
    app.register_blueprint(auth.bp)


    db.init_app(app)
    
    return app

if __name__ == "__main__":
    app=create_app()
    app.run(debug=True)
    
