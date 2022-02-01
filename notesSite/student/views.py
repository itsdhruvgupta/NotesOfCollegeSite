from logging.config import valid_ident
from math import fabs
from optparse import Values
from select import select
import string
from django.http import JsonResponse
from django.shortcuts import redirect, render , HttpResponse
from student.models import *


def index(request):

    studyMaterial_data = studyMaterial.objects.all()[:3]
    result_data = result.objects.all()[:4]
    notice_data = notice.objects.all()[:4]
    dict = {'studyMaterial_data':studyMaterial_data,'result_data':result_data,'notice_data':notice_data}
    return render(request,'index.html',dict)

def study_materials_page(request):
    
    if request.method == 'GET':
        select_course = request.GET.get('course','select')
        print(select_course)

        select_sem = request.GET.get('sem','select')
        print(select_sem)

        if select_sem == 'select' or select_course == 'select':
          

            if select_sem != 'select':
                studyMaterial_data = studyMaterial.objects.filter(uploader_sem=select_sem).values()
                dict = {'studyMaterial_data':studyMaterial_data}

            if select_course != 'select':
                studyMaterial_data = studyMaterial.objects.filter(uploader_course=select_course).values()
                dict = {'studyMaterial_data':studyMaterial_data}
                
            elif select_sem == 'select' and select_course == 'select':
                studyMaterial_data = studyMaterial.objects.all()
                dict = {'studyMaterial_data':studyMaterial_data}


        else:
            studyMaterial_data = studyMaterial.objects.filter(uploader_course=select_course ,uploader_sem = select_sem).values()
            dict = {'studyMaterial_data':studyMaterial_data}

    return render(request,'Study-Materials.html',dict)


def f_result(request):
    
    if request.method == 'GET':
        select_sem = request.GET.get("sem","select")
        select_course = request.GET.get("course" ,"select")
        print(select_sem, select_course)

        if select_sem == 'select' or select_course == 'select':
            if select_sem != 'select':
                print("select_sem")
                result_data = result.objects.filter(result_sem=select_sem)
                dict = {'result_data':result_data}

            if select_course != 'select':
                print("select_course")
                result_data = result.objects.filter(result_course=select_course)
                dict = {'result_data':result_data}
                
            elif select_sem == 'select' and select_course == 'select':
                result_data = result.objects.all()
                dict = {'result_data':result_data}

        else:
            result_data = result.objects.filter(result_course=select_course ,result_sem = select_sem)
            print("select_course")
            dict = {'result_data':result_data}

    return render(request,'result.html',dict)

def college_activites(request):
    
    return render(request,'college-activities.html')


def notice_board(request):
    notice_data = notice.objects.all()
    dict = {"notice_data":notice_data}

    return render(request,'notice_board.html',dict)

def f_bugs(request):
    
    return render(request,'report_bugs.html')

def eventpage(request):
    if request.method == "GET":
        post = post_data.objects.all()
        dict = {"post_data":post}
        return render(request,'Event-page.html',dict)
    if request.method == "POST":
        count = int(request.POST.get("count"))
        user = request.POST.get("user")
        post_data(username = user)
        likes = post_data.objects.filter(username = user)
        likes = (likes.values('likes'))
        likes = (likes[0].get('likes'))
        if(count == -1):
            likes = likes - 1
        else:
            likes = (likes + 1)
        p = post_data(likes = likes)
        likes = post_data.objects.filter(username = user).update(likes = likes)
        dict = {'msg' :'hello world'}
        return JsonResponse(dict)
        


def addStudyMaterial(request):
    
    return render(request,'addstudymaterial.html')


def quiz(request):
    return render(request, 'quiz.html')

def add_students(request):
    return render(request, 'add_students.html')