from flask import Blueprint

from beauty_admin.conf.db import db

bp = Blueprint('/', __name__)


@bp.route('/health')
def health():
    db.engine.execute('SELECT 1')
    return {}
