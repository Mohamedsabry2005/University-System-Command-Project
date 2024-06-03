import questionary
import add_student as s
import functions as fun
import os

print('Welcome to Our University system:')
while True:
    operation =questionary.select('Select operation: ',choices=['Show excel file','Courses','Students','Exit']).ask()
    if operation=='Exit':
        print('Exit....')
        break
    elif operation == 'Show excel file':
        os.system('cls')
        fun.table()
    elif operation =='Courses':
        courses=questionary.select('Select operation: ',choices=['Edit grades','Statistics','Sort (id)',"Add course"]).ask()
        if courses=='Edit grades':
            grades=questionary.select('Select operation: ',choices=['Enter grade','Update grade','Delete grade']).ask()
            if grades=='Enter grade':
                id=questionary.select('Select id: ',choices=s.id).ask()
                course=questionary.select('Select course: ',choices=fun.specificCourses(id)).ask()
                type=questionary.select("Select type: ",choices=['quiz','midterm',"final"]).ask()
                score=questionary.text('enter score: ').ask()
                if score.isnumeric():
                    fun.enter(id,course,type,score)
                else:
                    print('score must be numbers ')
            elif grades=='Update grade':
                id=questionary.select('Select id: ',choices=s.id).ask()
                course=questionary.select('Select course: ',choices=fun.specificCourses(id)).ask()
                type=questionary.select("Select type: ",choices=['quiz','midterm',"final"]).ask()
                score=questionary.text('enter score: ').ask()
                if score.isnumeric():
                    fun.update(id,course,type,score)
                else:
                    print('score must be numbers ')
            else:
                id=questionary.select('Select id: ',choices=s.id).ask()
                course=questionary.select('Select course: ',choices=fun.specificCourses(id)).ask()
                type=questionary.select("Select type: ",choices=['quiz','midterm',"final"]).ask()
                fun.delete(id,course,type)
        elif courses=='Statistics':
            stat=questionary.select('Select operation',choices=['Maximum','Minimum','Average','Median']).ask()
            if stat=='Maximum':
                course=questionary.select('Select course: ',choices=s.courses).ask()
                fun.maximum(course)
            elif stat=='Minimum':
                course=questionary.select('Select course: ',choices=s.courses).ask()
                fun.minimum(course) 
            elif stat=='Average':
                course=questionary.select('Select course: ',choices=s.courses).ask()
                fun.Average(course) 
            else:
                course=questionary.select('Select course: ',choices=s.courses).ask()
                fun.Median(course)
        elif courses=='Add course':
            course=questionary.text('enter course: ').ask()
            s.courses.append(course)
            fun.header.append(course)
            print('added') 
        else:
            fun.sort()
    else:
        student=questionary.select('Select operation: ',choices=['Enroll course','Withdraw course','GPA','Add Students']).ask()
        if student=='Enroll course':
            id=questionary.select('Select id: ',choices=s.id).ask()
            course=questionary.select('Select course: ',choices=fun.notAddCourses(id)).ask()
            fun.enroll(id,course)
        elif student=='Withdraw course':
            id=questionary.select('Select id: ',choices=s.id).ask()
            course=questionary.select('Select course: ',choices=fun.specificCourses(id)).ask()
            fun.withdraw(id,course)
        elif student=='Add Students':
            newid=questionary.text('enter new id :').ask()
            if newid.isnumeric():
                newname=questionary.text('enter name: ').ask()
                if newname.isalpha():
                    listCourses=questionary.checkbox("Select courses", choices=s.courses).ask()
                    fun.addStudent(newid,newname,listCourses)
                else:
                    print('name must be numbers only')
            else:
                print('id must be numbers only')
        else:
            id=questionary.select('Select id: ',choices=s.id).ask()
            fun.calculate_gpa(id)

