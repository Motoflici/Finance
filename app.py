from flask import Flask, render_template, redirect, url_for
from forms import CourseSimulator
import simulations

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

CourseName = []
CourseHours = []
CourseCost = []
CourseCompetitionRate = []
CourseLicenseCost = []
CourseStudents = []
CourseIterations = []
CourseTrainer = []
CourseTrainerRate = []
CourseStudentOperationalCost = []
courseMarketingCost = []
courseDeliveryCost = []
courseTotalLicenseCost = []
courseTotalOperationalCost = []
courseTotalRevenue = []
courseTotalCosts = []
courseProfit = []


@app.route('/', methods=('GET', 'POST'))
def index():
    form = CourseSimulator()
    if form.validate_on_submit():
        CourseName.append(form.denumireCurs.data)
        CourseHours.append(form.numarOre.data)
        CourseCost.append(form.costCurs.data)
        CourseCompetitionRate.append(form.costCompetitie.data)
        CourseLicenseCost.append(form.costLiceenta.data)
        CourseStudents.append(form.students.data)
        CourseIterations.append(form.iteratii.data)
        CourseTrainer.append(form.numeProfesor.data)
        CourseTrainerRate.append(form.tarifOrar.data)
        CourseStudentOperationalCost.append(form.costOperational.data)
        courseMarketingCost.append(form.costMarketing.data)
        for i in CourseName:
            x = int(CourseTrainerRate[i]) * int(CourseHours[i])
            courseDeliveryCost.append(x)
            t = int(CourseLicenseCost[i]) * int(CourseStudents[i]) * int(CourseIterations[i])
            courseTotalLicenseCost.append(t)
            p = int(CourseStudentOperationalCost[i]) * int(CourseStudents[i]) * int(CourseIterations[i])
            courseTotalOperationalCost.append(p)
            y = int(CourseCost[i]) * int(CourseStudents[i]) * int(CourseIterations[i])
            courseTotalRevenue.append(y)
            m = int(courseMarketingCost[i]) + int(courseTotalLicenseCost[i]) + int(courseDeliveryCost[i]) + int(courseTotalOperationalCost[i])
            courseTotalCosts.append(m)
            v = courseTotalRevenue - courseTotalCosts
            courseProfit.append(v)
            return courseDeliveryCost, courseTotalLicenseCost, courseTotalOperationalCost, courseTotalRevenue, courseTotalCosts, courseProfit
        return redirect(url_for('coursesKPI'))
    return render_template('index.html', form=form)


@app.route('/coursesKPI/')
def coursesKPI():
    return render_template('coursesKPI.html', CourseName=CourseName, CourseCost=CourseCost, CourseHours=CourseHours, CourseCompetitionRate=CourseCompetitionRate,
                           CourseLicenseCost=CourseLicenseCost, CourseStudents=CourseStudents, CourseIterations=CourseIterations,
                           CourseTrainer=CourseTrainer, CourseTrainerRate=CourseTrainerRate, CourseStudentOperationalCost=CourseStudentOperationalCost,
                           courseMarketingCost=courseMarketingCost, courseTotalOperationalCost=courseTotalOperationalCost, courseTotalLicenseCost=courseTotalLicenseCost,
                           courseTotalRevenue=courseTotalRevenue, courseProfit=courseProfit)
