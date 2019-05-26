from flask import render_template, Blueprint

bp = Blueprint('view', __name__, template_folder='templates')


@bp.route('/', methods=['GET'])
def index():
    # todo: response bundle file
    return render_template('index.html')
