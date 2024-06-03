import add_student as s
from prettytable import PrettyTable  
import csv
header=['id','name',"EAP-017",'MATH-1910','CS-1910','STAT-1910','EAP-011']
# start table
def table():
    """
    this function create table in terminal and generate CSV file
    """    
    with open('data.csv', "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        # excell file
        for id, data in s.students.items():
            student_row = [id, data["name"]]

            for course in header[2:]:
                dataset=data["courses"].get(course,{})
                total=dataset.get("quiz", '') + dataset.get("midterm", "") + dataset.get("final", "") 
                if total =="":
                    grade='not enrolled'
                    # grade=total
                else:
                    grade=total
                student_row.append(grade)

            writer.writerow(student_row)
        # showing table
    with open('data.csv','r',newline='')as csvfile:
        myTable = PrettyTable(header) 
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            myTable.add_row(row)
        print(myTable)
table()
# end table
#-------------------------------------------
# start edit grades
def enter(id,course,type,grade):
    """
    this function to enter grade for course
    """    
    if s.students[id]['courses'][course][type]==0:
        s.students[id]['courses'][course][type]=grade
        print('added')
    else:
        print('there is old grade')

def update(id,course,type,grade):
    """
    this function to update grade for course
    """    
    if type=='quiz':
        if float(grade) >10:
            print('quiz grade must be less than 10')
        else:
            s.students[id]['courses'][course][type]=float(grade)
    elif type=='midterm':
        if float(grade) >30:
            print('midterm grade must be less than 30')
        else:
            s.students[id]['courses'][course][type]=float(grade)
    else:
        if float(grade) >60:
            print('final grade must be less than 60')
        else:
            s.students[id]['courses'][course][type]=float(grade)

def delete(id,course,type):
    """
    this function to delete grade for course
    """ 
    s.students[id]['courses'][course][type]=0

# end edit grades
#-------------------------------------------
# start statistics
def maximum(course):
    """
    this function to calcualate the maximum grade in course
    """ 
    maximum=0
    ids=[]
    for id, data in s.students.items():
        if s.students[id]["courses"].get(course,0):
            if s.students[id]["courses"][course]['final']>maximum:
                maximum=s.students[id]["courses"][course]['final']
            if s.students[id]["courses"][course]['final']==maximum:
                ids.append(id)
    if ids:
        print(f'there are {len(ids)} ids {ids} have the same grade {maximum} ')
    else:
        print(f'maximum is {maximum} for student {id} and name is {data.get('name')}')


def minimum(course):
    """
    this function to calcualate the minimum grade in course
    """ 
    minimum=101
    ids=[]
    for id, data in s.students.items():
        if s.students[id]["courses"].get(course,0):
            if s.students[id]["courses"][course]['final']<minimum:
                minimum=s.students[id]["courses"][course]['final']
            if s.students[id]["courses"][course]['final']==minimum:
                ids.append(id)
    if ids:
        print(f'there are {len(ids)} ids {ids} have the same grade {minimum} ')
    else:
        print(f'minimum is {minimum} for student {id} and name is {data.get('name')}')


def Average(course):
    """
    this function to calcualate the average grade in course
    """ 
    total=0
    length=0
    for id in s.students.keys():
        if s.students[id]["courses"].get(course,0):
            total+=s.students[id]["courses"][course]['final']
            length+=1
    avg=total/length
    print(f"the average is {avg}")

def Median(course):
    """
    this function to calcualate the median grade in course
    """ 
    sort()
    listOfGrades=[]
    for id in s.students.keys():
        if s.students[id]["courses"].get(course,0):
            listOfGrades.append(s.students[id]["courses"][course]['final'])
    medianIndex=len(listOfGrades)//2
    median=listOfGrades[medianIndex]
    print(f'the median is {median}')
# end statistics
#----------------------------------
# start sort
def sort():
    """
    this function to sort data based on id order
    """ 
    s.students=dict(sorted(s.students.items()))
# end sort
#-------------------------------------
# start student
def withdraw(id, course):
    """
    this function to delete course from student
    """ 
    del s.students[id]["courses"][course]

def enroll(id,course):
    """
    this function to add course to student
    """ 
    s.students[id]['courses'][course]={'quiz':0,'midterm':0,'final':0}
# end student
# start add student
def addStudent(id,name,listCourses):
    """
    this function to add new student 
    """ 
    if id not in s.students:
        s.students[id]={
                'name':name,
                'courses':{}
            }
        for i in listCourses:
            s.students[id]["courses"][i]={'quiz':0,'midterm':0,'final':0}
    else:
        print('id must be unique')

# this is for user when enroll course,it shows only not enrolled courses
def notAddCourses(id):
    """
    this is for user when enroll course,it shows only not enrolled courses
    """
    courses=header[2:]
    idcourses=[]
    uniqueCourse=[]
    print(courses)
    for course in s.students[id]['courses']:
        idcourses.append(course)
    for course in courses:
        print(course)
        if course not in idcourses:
            uniqueCourse.append(course)
    return uniqueCourse
# end add student
# ----------------------------------------

def specificCourses(id):
    """
    this is for user to show only courses for specific id
    """
    courses=[]
    for course in s.students[id]['courses']:
        courses.append(course)
    return courses



def Hours(courses):
    """
    this function to calcualte the credit hourse for courses
    """
    creditHour=[]
    for i in courses:
        if i=="MATH-1910":
            creditHour.append({i:4})
        if i =="EAP-011" or i=="EAP-017":
            creditHour.append({i:0})
        else:
            creditHour.append({i:3})
    return creditHour

def calculate_gpa(id):
    """
    this function calcualte GPA for student
    """
    credit_hours=Hours(specificCourses(id))
    grade_scores = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    totalGrades = 0
    totalHours = 0
    grades=[]
    hours=[]
    for i in s.students[id]['courses']:
        grades.append(sum(s.students[id]['courses'][i].values()))
    for i in range(len(credit_hours)):
        hours.append(list(credit_hours[i].values()))

    for i in range(len(grades)):
            grade = grades[i]
            credit_hour = hours[i][0]
            if grade >90:
                grade_score = grade_scores['A']
                totalGrades += grade_score * credit_hour
                totalHours += credit_hour
            elif grade>80:
                grade_score = grade_scores['B']
                totalGrades += grade_score * credit_hour
                totalHours += credit_hour
            elif grade >70:
                grade_score = grade_scores['C']
                totalGrades += grade_score * credit_hour
                totalHours += credit_hour
            elif grade >60 or grade >50:
                grade_score = grade_scores['D']
                totalGrades += grade_score * credit_hour
                totalHours += credit_hour
            elif grade >40:
                grade_score = grade_scores['F']
                totalGrades += grade_score * credit_hour
                totalHours += credit_hour


    if totalHours == 0:
        return "No GPA"



    gpa = totalGrades / totalHours
    print(f"gpa is {gpa}")




