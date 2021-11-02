from django.shortcuts import redirect, render , HttpResponse
from student.models import studyMaterial
def index(request):
    return render(request,'index.html')

def study_materials(request):
    if request.method == 'POST':
        select_course = request.POST.get('course')
        select_sem = request.POST.get('sem')

        if select_sem == 'select' or select_course == 'select':
            print("kuch bhi")

            if select_sem != 'select':
                studyMaterial_data = studyMaterial.objects.filter(uploader_sem=select_sem)
                dict = {'studyMaterial_data':studyMaterial_data}
            if select_course != 'select':
                studyMaterial_data = studyMaterial.objects.filter(uploader_course=select_course)
                dict = {'studyMaterial_data':studyMaterial_data}
                
            elif select_sem == 'select' and select_course == 'select':
                print("lala")
                dict = {'studyMaterial_data':"studyMaterial_data"}
        else:
            studyMaterial_data = studyMaterial.objects.filter(uploader_course=select_course ,uploader_sem = select_sem)
            dict = {'studyMaterial_data':studyMaterial_data}

    else:
        studyMaterial_data = studyMaterial.objects.all()
        dict = {'studyMaterial_data':studyMaterial_data}
    
    
    return render(request,'Study-Materials.html',dict)

def college_activites(request):
    
    return render(request,'college-activities.html')
