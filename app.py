from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
from forms import CourseSimulator, SaleDetails
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
import matplotlib.pyplot as plt
from sqlalchemy import select, create_engine, text
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:FantasyTown1@localhost:3306/Test"
db = SQLAlchemy(app)


class Sales(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    client = db.Column(db.String(100))
    total = db.Column(db.Integer)
    workItem = db.Column(db.String(100))
    workDays = db.Column(db.Integer)


# def __init__(self, client, total, workItem, workDays):
#    self.client = client
#    self.total = total
#    self.workItem = workItem
#    self.workDays = workDays


with app.app_context():
    db.create_all()
engine = create_engine('mysql://root:FantasyTown1@localhost:3306/Test')

Session = sessionmaker(bind=engine)
session = Session()
engine.connect()

db.init_app(app)

courseList = [
]


@app.route('/', methods=('GET', 'POST'))
def index():
    form = CourseSimulator()
    # Pentru fiecare submit nou
    if form.validate_on_submit():
        # definit sablon dictionar (Course data)
        # -> Preluat valori form ca parametrii
        courseData = {"CourseName": form.denumireCurs.data, "CourseHours": form.numarOre.data,
                      "CourseCost": form.costCurs.data, "CourseLicenseCost": form.costLiceenta.data,
                      "CourseStudents": form.students.data, "CourseIterations": form.iteratii.data,
                      "CourseTrainer": form.numeProfesor.data, "CourseTrainerRate": form.tarifOrar.data,
                      "CourseStudentOperationalCost": form.costOperational.data,
                      "courseMarketingCost": form.costMarketing.data}
        # -> Calculate KPI's
        x = courseData["CourseTrainerRate"] * courseData["CourseHours"]
        courseData["courseDeliveryCost"] = x
        t = courseData["CourseLicenseCost"] * courseData["CourseStudents"] * courseData["CourseIterations"]
        courseData["courseTotalLicenseCost"] = t
        p = courseData["CourseStudentOperationalCost"] * courseData["CourseIterations"] * courseData["CourseStudents"]
        courseData["courseTotalOperationalCost"] = p
        y = courseData["CourseCost"] * courseData["CourseStudents"] * courseData["CourseIterations"]
        courseData["courseTotalRevenue"] = y
        m = courseData["courseMarketingCost"] + courseData["courseTotalOperationalCost"] + courseData[
            "courseTotalLicenseCost"] + (courseData["courseDeliveryCost"] * courseData["CourseIterations"])
        courseData["courseTotalCosts"] = m
        v = courseData["courseTotalRevenue"] - courseData["courseTotalCosts"]
        courseData["courseProfit"] = v
        # -> Append list with a new dictionary with values
        courseList.append(courseData)
        return redirect(url_for('coursesKPI', courseList=courseList))
    return render_template('index.html', form=form)


@app.route('/coursesKPI/')
def coursesKPI():
    return render_template('coursesKPI.html', courseList=courseList)


@app.route("/coursesKPI/", methods=['GET', 'POST'])
def ListClear():
    if request.method == 'POST':
        if request.form.get('Reset') == 'Reset':
            courseList.clear()
            return render_template("coursesKPI.html", courseList=courseList)
        else:
            # pass # unknown
            return render_template("coursesKPI.html")
    return render_template("coursesKPI.html")


simulationDict = []


@app.route("/priceSimulator/", methods=['GET', 'POST'])
def priceSimulator():
    if request.method == "POST":
        simulationData = {"Work item": request.form.get("workItem"),
                          "Work item type": request.form.get("workItemType"),
                          "complexity": request.form.get("complexity"),
                          "duration": request.form.get("duration")
                          }
        for i in simulationData.copy():
            if simulationData["Work item type"] == "B2B Courses":
                x = 1000
            else:
                x = 600
            simulationData["baseRate"] = x
            if simulationData["complexity"] == "High":
                y = 1.5
            elif simulationData["complexity"] == "Mid":
                y = 1.3
            else:
                y = 1.1
            simulationData["complexityFactor"] = y
            if int(simulationData["duration"]) < 5:
                z = 1.1
            else:
                z = 1
            simulationData["durationFactor"] = z
            t = x * y * z
            simulationData["simulatedRate"] = int(t)
        simulationDict.append(simulationData)
        return redirect(url_for('priceSimulator', simulationData=simulationData))
    return render_template("priceSimulator.html", simulationDict=simulationDict)


@app.route('/Sales/')
def sales():
    query = "SELECT id, client, total, workType, workDays FROM Sales;"
    result = engine.execute(text(query))
    return render_template("Sales.html", result=result)


@app.route('/saleDetails/<int:record_id>', methods=['GET', 'POST'])
def saleDetails(record_id):
    if request.method == 'POST':
        query = text("SELECT id, Client, total, workType, workDays FROM SALES WHERE id = :x;")
        result = engine.execute(query, x=record_id).fetchone()
        # record_id = request.form['record_id']
        return render_template("saleDetails.html", result=result)


@app.route('/saleDetails/<int:record_id>/update', methods=['GET', 'POST'])
def updateRecord(record_id):
    if request.method == 'POST':
        workType = request.form.get('workType')
        workDays = request.form.get('workDays')
        t = text("UPDATE Sales SET workType = :x, workDays = :y WHERE id = :z;")
        engine.execute(t, x=workType, y=workDays, z=record_id)
        session.commit()
        return redirect(url_for('sales'))


test = pd.read_sql_table('Sales', engine, 'Test')
test["dailyRate"] = test["total"] / test["workDays"]
courses = test[test["workType"] == 'Courses']
consultancy = test[test["workType"] == 'Consultancy']
coaching = test[test["workType"] == 'Coaching']

print(test, courses, consultancy, coaching)

if __name__ == "__main__":
    app.run(debug=True)
