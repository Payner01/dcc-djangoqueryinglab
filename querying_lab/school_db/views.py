from django.shortcuts import render
from .models import Student, Instructor, Course, StudentCourse


def index(request):
    students = Student.objects.all()

    # The following line creates a list that allows you to examine the data 
    # from a Queryset in an easier to visualize way
    # It is not required for functionality!
    # Place a breakpoint on line 14, then compare 'students' and 'data_visualization'
    data_visualization = [item for item in students]

    context = {
        'students': students
    }
    return render(request, 'school/index.html', context)

def problem_one(request):
    students = Student.objects.filter(gpa__gt=3.0).order_by('-gpa')
    # Find all students who have a GPA greater than 3.0. 
    # Order the data by highest GPAs first.
    data_visualization = [item for item in students]
    context = {
        'students': students
    }
    return render(request, 'school/one.html', context)

def problem_two(request):
    # Find all instructors hired prior to 2010
    # Order by hire date
    instructors = Instructor.objects.filter(hire_date__lt='2010-01-01').order_by('hire_date')
    data_visualization = [item for item in instructors]
    context = {
        'instructors': instructors
    }
    return render(request, 'school/two.html', context)

def problem_three(request):
    # Find all students who have a A+ in any class and are NOT getting a C+ in any class. 
    # Order the data by student's first name alphabetically.

    student_courses = StudentCourse.objects.filter(grade="A+")
    high_achievers = student_courses.exclude(student__studentcourse__grade="C+")
    data_visualization = [item for item in student_courses]
    context = {
        'student_courses': high_achievers
    }
    return render(request, 'school/three.html', context)

def problem_four(request):
    # Find all students who are taking the Programming class. 
    # Order by their grade. 
    programming_class = StudentCourse.objects.filter(course_id="4").order_by("grade")
    data_visualization = [item for item in programming_class]
    context = {
        'student_courses': programming_class
    }
    return render(request, 'school/four.html', context)


def problem_five(request):
    # Find all students getting an A in the Programming class. 
    # Order by last name.


    programming_class = StudentCourse.objects.filter(course_id="4")
    high_grade = programming_class.filter(grade='A').order_by('student__last_name')
    data_visualization = [item for item in programming_class]
    context = {
        'student_courses': high_grade
    }
    return render(request, 'school/five.html', context)

def problem_six(request):
    # Find all students with a GPA less than 3.0 who are getting an A in Programming class.
    # Order by GPA.

    context = {
        'student_courses': None
    }
    return render(request, 'school/six.html', context)

################## BONUS #################
# These problems will require using Aggregate functions along with annotate()
# https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
# https://docs.djangoproject.com/en/4.0/ref/models/querysets/#annotate

# Create a view function and template for each bonus problem you complete

# BONUS ONE
# Write a query to find any instructors who are only teaching one single course. Display the instructor and the course

# BONUS TWO
# Display all students along with the number of credits they are taking

# BONUS THREE
# Find all students who are getting an A in any course and average their GPAs. Display the number of students and their Average GPA

# BONUS FOUR
# Write a function that will replace student GPAs in the database with an accurate score based only on their current grades
# This may require multiple queries
# See https://www.indeed.com/career-advice/career-development/gpa-scale for a chart of what point value each grade is worth