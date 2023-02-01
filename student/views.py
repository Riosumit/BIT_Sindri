from django.shortcuts import render, redirect
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="",charset='utf8',database="BIT_Sindri")
# mydb = mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6586203",password="WduumesPgh",charset='utf8',database="sql6586203")
cursor=mydb.cursor()
# cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
# account = cursor.fetchone()
# mydb.commit()

# Create your views here.
def result(request):
    return render(request, 'result.html')

def registration(request):
    msg=''
    reg_no = request.POST.get('reg_no','')
    roll_no = request.POST.get('roll_no','')
    f_name = request.POST.get('f_name','')
    l_name = request.POST.get('l_name','')
    caste = request.POST.get('caste','')
    gender = request.POST.get('gender','')
    father = request.POST.get('father','')
    father_occ = request.POST.get('father_occ','')
    mother = request.POST.get('mother','')
    mother_occ = request.POST.get('mother_occ','')
    degree = request.POST.get('degree','')
    course = request.POST.get('course','')
    year = request.POST.get('year','')
    semester = request.POST.get('semester','')
    if(f_name != ''):
        cursor.execute('SELECT * FROM student WHERE reg_no = %s OR roll_no = %s', (reg_no, roll_no,))
        student = cursor.fetchone()
        if student :
            msg = "Student already exists"
        else:
            cursor.execute('INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (reg_no, roll_no, f_name, l_name, caste, gender, father, father_occ, mother, mother_occ, degree, course, year, semester))
            mydb.commit()
            return redirect('result')
    cursor.execute('SELECT * FROM degree')
    degrees = cursor.fetchall()
    cursor.execute('SELECT * FROM course')
    courses = cursor.fetchall()
    param = {'msg':msg, 'reg_no':reg_no, 'roll_no':roll_no, 'f_name':f_name, 'l_name':l_name, 'caste':caste, 'gender':gender, 'father':father, 'father_occ':father_occ, 'mother':mother, 'mother_occ':mother_occ, 'course':courses, 'degree':degrees, 'year':year, 'semester':semester}
    return render(request, 'registration.html', param)