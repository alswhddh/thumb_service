from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def index():
    #id 값을 기준으로 내림차순 정렬
    return redirect(url_for('thumb._list'))