import numpy as np
from flask import Flask, render_template, session, redirect, url_for, request
from joblib import load
import pandas as pd

from forms import NutriscoreForm



app = Flask(__name__)
app.config['SECRET_KEY'] = b'E\x08#\xbb\x89Y#\xfa|%\x811\x7f\xf8B\xdc'


@app.route('/')
def index():
    return render_template('index.html', title='Accueil')


@app.route('/profil')
def profil():
    return render_template('profil.html', title='Votre profil')


@app.route('/blog')
def blog():
    return "blog"


@app.route('/faq')
def faq():
    return render_template('faq.html', title='formulaire')


@app.route('/nutri')
def nutri():
    return render_template('nutri.html', title='formulaire')


@app.route('/nutriscore')
def nutriscore():
    form = NutriscoreForm()
    if form.validate_on_submit():
        print(request.form)

    return render_template('nutriscore.html', title='Register')


@app.route('/score', methods=["get", "post"])
def score():
    return render_template('score.html', title='le score')


@app.route('/login')
def login():
    session['user'] = {
        'username': 'Rayane',
        'email': 'michel@dupont.com'
    }
    session['user']['role'] = 'admin'
    return redirect(url_for('index'))


@app.route('/post_log', methods=['get', 'post'])
def loginn():
    energy_100g = request.form['energy_100g']
    fat_100g = request.form['fat_100g']
    saturated_fat_100g = request.form['saturated_fat_100g']
    carbohydrates_100g = request.form['carbohydrates_100g']
    fibre_100g = request.form['fibre_100g']
    proteins_100g = request.form['proteins_100g']
    salt_100g = request.form['salt_100g']
    print('energy_100g:', energy_100g, 'fat_100g:', fat_100g, 'saturated_fat_100g:', saturated_fat_100g,
          'carbohydrates_100g:', carbohydrates_100g, 'fibre_100g:', fibre_100g, 'proteins_100g:', proteins_100g,
          'salt_100g:', salt_100g)

    df = pd.DataFrame(np.array(
        [[energy_100g, fat_100g, saturated_fat_100g, carbohydrates_100g, fibre_100g, proteins_100g, salt_100g]])
                      , columns=['energy_100g', 'fat_100g', 'saturated-fat_100g', 'carbohydrates_100g', 'fiber_100g',
                                 'proteins_100g', 'salt_100g'])

    dtree_model = load('nutriscore.joblib')
    produitnut = [[energy_100g, fat_100g, saturated_fat_100g, carbohydrates_100g, fibre_100g, proteins_100g, salt_100g]]
    model = load('nutriscore.joblib')
    prediction = model.predict(produitnut)


    return render_template('prediction.html', data=prediction)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/register', methods=['get', 'post'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(
            f'Email:{form.email.data} Password:{form.password.data} Amount:{form.amount.data} Magie:{form.magie.data}')

        return redirect(url_for('index'))
    return render_template('register.html', form=form, title='Register')
