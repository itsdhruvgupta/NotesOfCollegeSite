from select import select
from django.http import JsonResponse
from django.shortcuts import redirect, render , HttpResponse
from student.models import studyMaterial, result, notice



def index(request):

    studyMaterial_data = studyMaterial.objects.all()[:3]
    result_data = result.objects.all()[:4]
    notice_data = notice.objects.all()[:4]
    dict = {'studyMaterial_data':studyMaterial_data,'result_data':result_data,'notice_data':notice_data}
    return render(request,'index.html',dict)

def study_materials_page(request):
    
    if request.method == 'POST':
        select_course = request.POST.get('course')
        print(select_course)

        select_sem = request.POST.get('sem')
        print(select_sem)

        if select_sem == 'select' or select_course == 'select':
          

            if select_sem != 'select':
                studyMaterial_data = studyMaterial.objects.filter(uploader_sem=select_sem).values()
                data = list(studyMaterial_data)
                print("sems")
                dict = {'studyMaterial_data':data}
                return JsonResponse(dict);

            if select_course != 'select':
                studyMaterial_data = studyMaterial.objects.filter(uploader_course=select_course).values()
                data = list(studyMaterial_data)
                print("course")
                dict = {'studyMaterial_data':data}
                return JsonResponse(dict);
                
            elif select_sem == 'select' and select_course == 'select':
                
                dict = {'studyMaterial_data':""}
                return JsonResponse(dict);

        else:
            studyMaterial_data = studyMaterial.objects.filter(uploader_course=select_course ,uploader_sem = select_sem).values()
            print(studyMaterial_data)

            data = list(studyMaterial_data)
            print(data)

            print("all get")
            dict = {'studyMaterial_data':data}
            return JsonResponse(dict);


    else:
        studyMaterial_data = studyMaterial.objects.all()
        dict = {'studyMaterial_data':studyMaterial_data}

    return render(request,'Study-Materials.html',dict)


def f_result(request):
    if request.method == 'POST':
        select_course = request.POST.get('course')
        select_sem = request.POST.get('sem')
        print(select_course , select_sem)

        if select_sem == 'select' or select_course == 'select':
            if select_sem != 'select':
                result_data = result.objects.filter(result_sem=select_sem).values()
                data = list(result_data)
                dict = {'result_data':data}
                return JsonResponse(dict)

            if select_course != 'select':
                result_data = result.objects.filter(result_course=select_course).values()
                data = list(result_data)
                dict = {'result_data':data}
                return JsonResponse(dict)
                
            elif select_sem == 'select' and select_course == 'select':
                
                dict = {'result_data':""}
                return JsonResponse(dict)

        else:
            result_data = result.objects.filter(result_course=select_course ,result_sem = select_sem).values()
            data = list(result_data)
            dict = {'result_data':data}
            return JsonResponse(dict)

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
    
    return render(request,'Event-page.html')