from flask import Flask
from flask import render_template
from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from beauty_admin import __version__
from beauty_admin.api.base import bp
from beauty_admin.conf.db import db
from beauty_admin.conf.settings import settings
from beauty_models.beauty_models.models import Attachment
from beauty_models.beauty_models.models import Booking
from beauty_models.beauty_models.models import Business
from beauty_models.beauty_models.models import Location
from beauty_models.beauty_models.models import Merchant
from beauty_models.beauty_models.models import Offer
from beauty_models.beauty_models.models import User
from beauty_models.beauty_models.models import WorkingHours


def index():
    return render_template('index.html')


def _init_views(admin: 'Admin') -> None:
    admin.add_view(ModelView(Attachment, session=db.session))
    admin.add_view(ModelView(Booking, session=db.session))
    admin.add_view(ModelView(Business, session=db.session))
    admin.add_view(ModelView(Location, session=db.session))
    admin.add_view(ModelView(Merchant, session=db.session))
    admin.add_view(ModelView(Offer, session=db.session))
    admin.add_view(ModelView(User, session=db.session))
    admin.add_view(ModelView(WorkingHours, session=db.session))


def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = settings.DEBUG
    app.config['SECRET_KEY'] = settings.SECRET_KEY
    app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.sqlalchemy_database_uri

    admin = Admin(
        app,
        name=f'Reserve Admin {__version__}',
        template_mode='bootstrap4',
        index_view=AdminIndexView(),
        base_template='master.html',
    )
    db.init_app(app)
    app.register_blueprint(bp)
    app.route('/')(index)
    app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
    _init_views(admin)
    return app
