"""notesSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from student import views


urlpatterns = [
    path("",views.index, name = "home"),
    path("study-materials",views.study_materials_page, name = "study_materials_page"),

    path("notice-board",views.notice_board, name = "notice-board"),
    path("result",views.f_result, name = "result"),
    path("bugs",views.f_bugs, name = "bugs"),
    path("eventpage",views.eventpage, name = "eventpage"),
    path("addstudymaterial",views.addStudyMaterial, name = "addStudyMaterial"),
    path("quiz",views.quiz, name = "quiz")

    

]
