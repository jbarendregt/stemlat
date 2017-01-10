from flask import flash, Markup, redirect, render_template, url_for
from . import main
from ..models import Party
#from .forms import SiteForm, VisitForm
#from .models import db, query_to_list, Site, Visit

#main = Blueprint("main", __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/parties')
def parties():
    parties = Party.query
    return render_template('parties.html', parties=parties)
