from flask import render_template, request, flash, redirect, url_for
from cap import app
from cap.utils_get_data import airly_data
from cap.forms import RegistrationForm, LoginForm


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    cities = ['city_1', 'city_2', 'city_3']
    city_info = []
    for city in cities:
        given_city = request.form.get(city)
        if given_city:
            city_data = airly_data(given_city)
            values = city_data['values']
            indexes = city_data['indexes']
            norms = city_data['standards']
            city_info.append([given_city, values, indexes, norms])
    return render_template("home.html", city_info=city_info)


@app.route("/comparison")
def compare():
    return render_template("compare.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)
