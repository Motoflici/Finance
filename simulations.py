courseName = []
courseCost = []
courseCompetitionRate = []
courseHours = []
courseStudents = []
courseIterations = []
courseLicenseCost = []
courseMarketingCost = []
courseTrainer = []
courseTrainerRate = []
courseStudentOperationalCost = []
courseDeliveryCost = []
courseTotalLicenseCost = []
courseTotalOperationalCost = []
courseTotalRevenue = []
courseTotalCosts = []
courseProfit = []


def calculateCourseSimulationKPI():
    for i in courseName:
        x = courseTrainerRate[i] * courseHours[i]
        courseDeliveryCost.append(x)
        t = courseLicenseCost[i] * courseStudents[i] * courseIterations[i]
        courseTotalLicenseCost.append(t)
        p = courseStudentOperationalCost[i] * courseIterations[i] * courseStudents[i]
        courseTotalOperationalCost.append(p)
        y = courseCost[i] * courseStudents[i] * courseIterations[i]
        courseTotalRevenue.append(y)
        m = (courseMarketingCost[i] + courseTotalOperationalCost[i] + courseTotalLicenseCost[i] + (
                    courseDeliveryCost[i] * courseIterations[i]))
        courseTotalCosts.append(m)
        v = courseTotalRevenue[i] - courseTotalCosts[i]
        courseProfit.append(v)
    return courseDeliveryCost, courseTotalLicenseCost, courseTotalOperationalCost, courseTotalRevenue, courseTotalCosts, courseProfit

# course_data = {}
 #       course_data['courseDeliveryCost'] = int(int(course_data.get('courseTrainerRate')) * int(course_data.get('courseHours')))
 #       course_data['courseTotalLicenseCost'] = course_data['courseLicenseCost'] * course_data['courseStudents'] * \
  #                                              course_data['courseIterations']
  #      course_data['courseTotalOperationalCost'] = course_data['CourseStudents'] * course_data['CourseIterations'] * \
 #                                                   course_data['CourseStudentOperationalCost']
 #       course_data['courseTotalRevenue'] = course_data['CourseCost'] * course_data['CourseStudents'] * \
 #                                           course_data['CourseIterations']
 #       course_data['courseTotalCosts'] = course_data['courseDeliveryCost'] + course_data[
 #           'courseTotalOperationalCost'] + \
  #                                        course_data['courseTotalLicenseCost'] + course_data['courseMarketingCost']
  #      course_data['courseProfit'] = course_data['courseTotalRevenue'] - course_data['courseTotalCosts']