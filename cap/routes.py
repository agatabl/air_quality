from flask import render_template, request
from cap import app
from cap.utils import airly_data, osm_data


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
            # return render_template("home.html", cities=cities, values=values, indexes=indexes, norms=norms, given_city=given_city)
    # return render_template("home.html")
@app.route("/comparison")
def compare():


    return render_template("compare.html")
