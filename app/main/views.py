from flask import flash, Markup, redirect, render_template, url_for
from . import main
from ..models import Party, Opinion, Theme, Topic
from .forms import PartyForm, TopicForm, ThemeForm, IndexForm
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    parties = Party.query
    themes = Theme.query
    return render_template('index.html', form=form)

@main.route('/parties', methods=['GET', 'POST'])
def parties():
    parties = Party.query
    form = PartyForm()
    if form.validate_on_submit():
        party = Party(party_name=form.party_name.data)
        db.session.add(party)
    return render_template('parties.html', parties=parties, form=form)

@main.route('/delete-party/<int:id>', methods=['GET', 'POST'])
def delete_party(id):
    party = Party.query.filter_by(id=id).first_or_404()
    db.session.delete(party)
    return redirect('parties')

@main.route('/edit-party/<int:id>', methods=['GET', 'POST'])
def edit_party(id):
    party = Party.query.filter_by(id=id).first_or_404()
    form = PartyForm()
    if form.validate_on_submit():
        party.party_name = form.party_name.data
        db.session.add(party)
        return redirect('parties')
    form.party_name.data = party.party_name
    return render_template('edit.html', form=form)

@main.route('/topics', methods=['GET', 'POST'])
def topics():
    #topics = Topic.query.order_by('theme_id')
    topics = db.session.query(Topic).join(Theme).order_by(Theme.theme_name).all()
    themes = Theme.query
    form = TopicForm()
    form.theme.choices = [(t.id, t.theme_name) for t in Theme.query.order_by('theme_name')]
    if form.validate_on_submit():
        topic = Topic(topic_name=form.topic_name.data,
                    theme_id=form.theme.data)
        db.session.add(topic)
    return render_template('topics.html', topics=topics, themes=themes, form=form)

@main.route('/delete-topic/<int:id>', methods=['GET', 'POST'])
def delete_topic(id):
    topic = Topic.query.filter_by(id=id).first_or_404()
    db.session.delete(topic)
    return redirect('topics')

@main.route('/edit-topic/<int:id>', methods=['GET', 'POST'])
def edit_topic(id):
    form = TopicForm()
    form.theme.choices = [(t.id, t.theme_name) for t in Theme.query.order_by('theme_name')]
    topic = Topic.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        topic.topic_name = form.topic_name.data
        db.session.add(topic)
        return redirect('topics')
    form.topic_name.data = topic.topic_name
    return render_template('edit.html', form=form)

@main.route('/themes', methods=['GET', 'POST'])
def themes():
    themes = Theme.query
    themeform = ThemeForm()
    if themeform.validate_on_submit():
        theme = Theme(theme_name=themeform.theme_name.data)
        db.session.add(theme)
    return render_template('themes.html', themes=themes, themeform=themeform)

@main.route('/delete-theme/<int:id>', methods=['GET', 'POST'])
def delete_theme(id):
    theme = Theme.query.filter_by(id=id).first_or_404()
    db.session.delete(theme)
    return redirect('themes')

@main.route('/edit-theme/<int:id>', methods=['GET', 'POST'])
def edit_theme(id):
    form = ThemeForm()
    theme = Theme.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        theme.theme_name = form.theme_name.data
        db.session.add(theme)
        return redirect('themes')
    form.theme_name.data = theme.theme_name
    return render_template('edit.html', form=form)
