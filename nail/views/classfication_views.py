from flask import Blueprint, render_template , request
from sqlalchemy import func

bp = Blueprint('class',__name__,url_prefix='/class')

@bp.route('/')
def _class():
    return render_template('thumbnail/classfication.html')


