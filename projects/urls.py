from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('students', views.allStudents, name="allStudents"),
    path('student/<str:pk>', views.studentProfile, name="user-profile"),
    path('create-student', views.createStudent, name="createStudent"),
    path('update-student/<str:pk>', views.updateStudent, name="updateStudent"),
    path('delete-student/<str:pk>', views.deleteStudent, name="deleteStudent"),

    path('courses', views.allCourses, name="allCourses"),
    path('course/<str:pk>', views.courseProfile, name="course-profile"),
    path('create-course', views.createCourse, name="createCourse"),
    path('update-course/<str:pk>', views.updateCourse, name="updateCourse"),
    path('delete-course/<str:pk>', views.deleteCourse, name="deleteCourse"),

    path('contents', views.allContents, name="allContents"),
    path('create-content', views.createContent, name="createContent"),
    path('update-content/<str:pk>', views.updateContent, name="updateContent"),
    path('delete-content/<str:pk>', views.deleteContent, name="deleteContent"),

    path('submit-registration', views.submitRegistration, name="submitRegistration"),
]

