import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'


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
    hourlyComparison = (int(courseHourCost)/int(competitionHourly))
    revenue = (int(studenti) * int(iteratii) * int(pret))/5
    calculateLicenseCost = int(costLiceenta) * int(studenti) * int(iteratii)
    calculateDeliveryCost = (int(rate) * int(durata) * int(iteratii))
    calculateOperationalCost = (int(operational) * int(studenti) * int(iteratii))
    costs = calculateDeliveryCost + int(marketing) + calculateOperationalCost + calculateLicenseCost
    profit = revenue - costs
    profitMargin = (int(profit)/int(revenue))
    return render_template('result.html', revenue=revenue, costs=costs, profit=profit, margin=profitMargin, hourly=courseHourCost, competition=hourlyComparison, licenseCost=calculateLicenseCost, deliveryCost=calculateDeliveryCost, operationalCost=calculateOperationalCost)
