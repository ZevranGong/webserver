from flask import render_template, flash, redirect,make_response
from app import app
from .forms import RequestForm
from .algo import algo

@app.route('/')
@app.route('/index')
def index():
    # the following strings are for testing purposes
    user = {'nickname': 'Miguel'}
    post = {'prompt': 'Joy is the birth of interconnectedness, and of us. \
    Consciousness consists of chaos-driven reactions of quantum energy. \
    “Quantum” means a deepening of the Vedic. We live, we live, we are reborn.\
    Without serenity, one cannot reflect.\
    Greed is born in the gap where interconnectedness has been excluded. \
    Discontinuity is the antithesis of insight.'}
    return redirect('/request')

@app.route('/request', methods = ['GET', 'POST'])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        flash('Your request of "%s" has been submitted' % (form.req.data))
        flash('And your response is %s' % (str(algo(form.req.data))))
        #return render_template("index.html",title='Home',post = str(algo(form.req.data)))
        return render_template('forms.html', 
        title = 'request',
        form = form)
    return render_template('forms.html', 
        title = 'request',
        form = form)

