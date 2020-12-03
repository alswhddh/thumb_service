from flask import Blueprint, render_template , request
from sqlalchemy import func

from ..models import thumbnail

bp = Blueprint('thumb',__name__,url_prefix='/thumb')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    so = request.args.get('so', type=str, default='score')
    ca = request.args.get('ca',type=str)

    #카테고리
    if ca =='politics':
        if so == 'relation':
            thumb_list = thumbnail.query.order_by(thumbnail.title.desc()).filter(thumbnail.category == "정치.사회.경제")
        elif so == 'views':
            thumb_list = thumbnail.query.order_by(thumbnail.views.desc()).filter(thumbnail.category == "정치.사회.경제")
        else:
            thumb_list = thumbnail.query.order_by(thumbnail.score.desc()).filter(thumbnail.category == "정치.사회.경제")
    elif ca =='beauti':
        if so == 'relation':
            thumb_list = thumbnail.query.order_by(thumbnail.title.desc()).filter(thumbnail.category == "패션.뷰티.스타일")
        elif so == 'views':
            thumb_list = thumbnail.query.order_by(thumbnail.views.desc()).filter(thumbnail.category == "패션.뷰티.스타일")
        else:
            thumb_list = thumbnail.query.order_by(thumbnail.score.desc()).filter(thumbnail.category == "패션.뷰티.스타일")
    elif ca =='trip':
        if so == 'relation':
            thumb_list = thumbnail.query.order_by(thumbnail.title.desc()).filter(thumbnail.category == "여행.관광")
        elif so == 'views':
            thumb_list = thumbnail.query.order_by(thumbnail.views.desc()).filter(thumbnail.category == "여행.관광")
        else:
            thumb_list = thumbnail.query.order_by(thumbnail.score.desc()).filter(thumbnail.category == "여행.관광")
    else:
        if so == 'relation':
            thumb_list = thumbnail.query.order_by(thumbnail.title.desc()).filter(thumbnail.category == "먹방.ASMR")
        elif so == 'views':
            thumb_list = thumbnail.query.order_by(thumbnail.views.desc()).filter(thumbnail.category == "먹방.ASMR")
        else:
            thumb_list = thumbnail.query.order_by(thumbnail.score.desc()).filter(thumbnail.category == "먹방.ASMR")

    # 검색
    if kw:
        search = '%%{}%%'.format(kw)

        thumb_list = thumb_list \
            .filter(thumbnail.title.ilike(search) |  # 제목
                    thumbnail.youtuber.ilike(search)  # 유튜버
                    )\
            .distinct()

    thumb_list = thumb_list.paginate(page, per_page=10)
    return render_template('thumbnail/thumb_list.html',thumb_list=thumb_list,page=page, kw=kw,so=so,ca=ca)