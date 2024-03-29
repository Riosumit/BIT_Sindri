from urllib import request
from django.shortcuts import render, redirect
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="",charset='utf8',database="BIT_Sindri")
# mydb = mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6586203",password="WduumesPgh",charset='utf8',database="sql6586203")
cursor=mydb.cursor()
# cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
# account = cursor.fetchone()
# mydb.commit()

# Create your views here.
def login(request):
    try:
        loggedin = request.session['loggedin']
    except:
        loggedin = False
    if loggedin:
        return redirect('admin_home')
    else:
        msg=''
        name = request.POST.get('name','')
        password = request.POST.get('password','')
        if(name != '' and password != ''):
            if(name == "admin" and password == "admin@123"):
                request.session['loggedin'] = True
                return redirect('admin_home')
            else:
                msg = "Invalid Username or Password"
        param = {'msg':msg}
        return render(request, 'admin_login.html', param)

def admin_home(request):
    try:
        loggedin = request.session['loggedin']
    except:
        loggedin = False
    if loggedin == False:
        return redirect('')
    return render(request, 'admin_home.html')

def degree(request):
    del_item = request.POST.get('del_item','')
    print(del_item)
    if(del_item != ""):
        cursor.execute("DELETE FROM degree WHERE name = %s", (del_item,))
    cursor.execute("SELECT * FROM degree")
    degrees = cursor.fetchall()
    param = {'degrees':degrees}
    return render(request, 'degrees.html', param)

def add_degree(request):
    msg = ''
    name = request.POST.get('name', '')
    duration = request.POST.get('duration','')
    if(name != '' and duration != ''):
        cursor.execute('SELECT * FROM degree WHERE name = %s', (name,))
        degree = cursor.fetchone()
        if degree:
            msg = 'degree already exists'
        else:
            cursor.execute('INSERT INTO degree VALUES(%s, %s)', (name, duration,))
            mydb.commit()
            name=''
            duration=''
            msg = 'degree Added Succesfully'
    param = {'msg':msg}
    return render(request, 'add_degree.html', param)

def course(request):
    del_item = request.POST.get('del_item','')
    print(del_item)
    if(del_item != ""):
        cursor.execute("DELETE FROM course WHERE name = %s", (del_item,))
    cursor.execute("SELECT * FROM course")
    courses = cursor.fetchall()
    param = {'courses':courses}
    return render(request, 'courses.html', param)

def add_course(request):
    msg = ''
    name = request.POST.get('name', '')
    deg = request.POST.get('degree','')
    nos = request.POST.get('nos','')
    if(name != '' and deg != '' and nos != ''):
        cursor.execute('SELECT * FROM course WHERE name = %s', (name,))
        course = cursor.fetchone()
        if course:
            msg = 'course already exists'
        else:
            cursor.execute('INSERT INTO course VALUES(%s, %s, %s)', (name, deg, nos,))
            mydb.commit()
            name=''
            duration=''
            msg = 'course Added Succesfully'
    cursor.execute('SELECT * FROM degree')
    degree = cursor.fetchall()
    param = {'msg':msg, 'degree': degree}
    return render(request, 'add_course.html', param)

def link(request):
    del_item = request.POST.get('del_item','')
    Activate = request.POST.get('Activate','')
    Deactivate = request.POST.get('Deactivate','')
    URL = request.get_host()
    if(del_item != ""):
        cursor.execute("DELETE FROM links WHERE name = %s", (del_item,))
    if(Activate != ""):
        cursor.execute("UPDATE links SET status = %s WHERE name = %s", ("Active", Activate))
    if(Deactivate != ""):
        cursor.execute("UPDATE links SET status = %s WHERE name = %s", ("Passive", Deactivate))
    cursor.execute("SELECT * FROM links")
    links = cursor.fetchall()
    param = {'links':links, 'URL': URL}
    return render(request, 'links.html', param)

def add_link(request):
    msg = ''
    name = request.POST.get('name', '')
    li = request.POST.get('link','')
    status = request.POST.get('status','')
    if(name != '' and li != ''):
        cursor.execute('SELECT * FROM links WHERE name = %s', (name,))
        link = cursor.fetchone()
        if link:
            msg = 'Link already exists'
        else:
            cursor.execute('INSERT INTO links VALUES(%s, %s, %s)', (name, li, status,))
            mydb.commit()
            name=''
            duration=''
            msg = 'Link Added Succesfully'
    param = {'msg':msg,}
    return render(request, 'add_link.html', param)