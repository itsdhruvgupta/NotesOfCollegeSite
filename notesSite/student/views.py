from django.shortcuts import redirect, render , HttpResponse
from student.models import studyMaterial
def index(request):
    return render(request,'index.html')

def select_course(request):
    studyMaterial_data = studyMaterial.objects.all()
    dict = {'studyMaterial_data':studyMaterial_data}
    return render(request,'course.html',dict)

def college_activites(request):
    return render(request,'college-activities.html')
