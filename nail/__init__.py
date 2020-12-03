from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

#db, migrate 전역변수로 선언
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    #config.py 에서 작성한 항목들을 app.config 환경변수로 읽어들임
    app.config.from_object(config)

    #객체 초기화
    db.init_app(app)
    migrate.init_app(app,db)

    from . import models

    from .views import main_views , thumb_views, classfication_views, similartly_views #,viewsPredict_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(thumb_views.bp)
    app.register_blueprint(classfication_views.bp)
    # app.register_blueprint(viewsPredict_views.bp)
    app.register_blueprint(similartly_views.bp)

    return app