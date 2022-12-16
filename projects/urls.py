from django.urls import path
from . import views

urlpatterns = [
    path('', views.practices, name="practices"),
    path('practice-3/', views.practice_three, name="practice_3"),
    path('practice-4/', views.practice_four, name="practice_4"),

    path('students', views.allStudents, name="allStudents"),
    path('create-student', views.createStudent, name="createStudent"),
    path('update-student/<str:pk>', views.updateStudent, name="updateStudent"),
    path('delete-student/<str:pk>', views.deleteStudent, name="deleteStudent"),

    path('cources', views.allCources, name="allCources"),
    path('create-cource', views.createCource, name="createCource"),
    path('update-cource/<str:pk>', views.updateCource, name="updateCource"),
    path('delete-cource/<str:pk>', views.deleteCource, name="deleteCource"),

    path('submit-registration', views.submitRegistration, name="submitRegistration"),

]

