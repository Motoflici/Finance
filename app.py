from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import form

from forms import CourseSimulator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# definit lista container (lista de dictionare)
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
                      "CourseCost": form.costCurs.data,
                      "CourseCompetitionRate": form.costCompetitie.data, "CourseLicenseCost": form.costLiceenta.data,
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
