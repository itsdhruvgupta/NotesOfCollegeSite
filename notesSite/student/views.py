from django.shortcuts import redirect, render , HttpResponse
from student.models import studyMaterial, result
def index(request):
    return render(request,'index.html')

def study_materials(request):
    if request.method == 'POST':
        select_course = request.POST.get('course')
        select_sem = request.POST.get('sem')

        if select_sem == 'select' or select_course == 'select':
          

            if select_sem != 'select':
                studyMaterial_data = studyMaterial.objects.filter(uploader_sem=select_sem)
                dict = {'studyMaterial_data':studyMaterial_data}
            if select_course != 'select':
                studyMaterial_data = studyMaterial.objects.filter(uploader_course=select_course)
                dict = {'studyMaterial_data':studyMaterial_data}
                
            elif select_sem == 'select' and select_course == 'select':
                
                dict = {'studyMaterial_data':""}
        else:
            studyMaterial_data = studyMaterial.objects.filter(uploader_course=select_course ,uploader_sem = select_sem)
            dict = {'studyMaterial_data':studyMaterial_data}

    else:
        studyMaterial_data = studyMaterial.objects.all()
        dict = {'studyMaterial_data':studyMaterial_data}

    return render(request,'Study-Materials.html',dict)


def f_result(request):
    if request.method == 'POST':
        select_course = request.POST.get('course')
        select_sem = request.POST.get('sem')

        if select_sem == 'select' or select_course == 'select':
          

            if select_sem != 'select':
                result_data = result.objects.filter(result_sem=select_sem)
                dict = {'result_data':result_data}
            if select_course != 'select':
                result_data = result.objects.filter(result_course=select_course)
                dict = {'result_data':result_data}
                
            elif select_sem == 'select' and select_course == 'select':
                
                dict = {'result_data':""}
        else:
            result_data = result.objects.filter(result_course=select_course ,result_sem = select_sem)
            dict = {'result_data':result_data}

    else:
        result_data = result.objects.all()
        dict = {'result_data':result_data}
    
    
    return render(request,'result.html',dict)

def college_activites(request):
    
    return render(request,'college-activities.html')


def notice_board(request):
    
    return render(request,'notice_board.html')
