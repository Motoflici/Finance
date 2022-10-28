import datetime
from markupsafe import escape
from flask import Flask, abort, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '9054ee8e382fae3ae8f01b0e249015c19bbc48cc67d13fd4'


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())



messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]


@app.route('/webform/')
def webform():
    return render_template('webform.html', messages=messages)


# ...

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)


# ...

# ...

@app.route('/courseSimulation/')
def courseSimulation():
    return render_template('courseSimulation.html')


@app.route('/courseSimulation/', methods=['POST'])
def courseSimulation_post():
    pret = request.form['pret']
    durata = request.form['durata']
    costLiceenta = request.form['license']
    rate = request.form['rate']
    studenti = request.form['studenti']
    iteratii = request.form['iteratii']
    marketing = request.form['marketing']
    operational = request.form['operational']
    competitionHourly = request.form['competition']
    courseHourCost = (int(pret)/int(durata))/5
    hourlyComparison = (int(competitionHourly)/int(courseHourCost))
    revenue = (int(studenti) * int(iteratii) * int(pret))/5
    costs = (int(durata) * int(rate) * int(iteratii)) + int(marketing) + (int(operational) * int(studenti) * int(iteratii)) + (int(costLiceenta) * int(studenti) * int(iteratii))
    profit = revenue - costs
    profitMargin = (int(profit)/int(revenue))
    return render_template('result.html', revenue=revenue, costs=costs, profit=profit, margin=profitMargin, hourly=courseHourCost, competition=hourlyComparison)


