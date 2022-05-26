from flask import Blueprint


bp = Blueprint('auth', __name__, url_prefix='/api')


@bp.get('/auth')
def get():
    return {'username': 'username'}
