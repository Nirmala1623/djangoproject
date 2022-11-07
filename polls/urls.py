from django.urls import include,path
from .import views
urlpatterns = [
    path('',views.student_details,name='student_details'),
]