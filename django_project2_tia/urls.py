from django.contrib import admin
from django.urls import path
from app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_numbers),
    path('subtract/', views.subtract_numbers),
    path('multiply/', views.multiply_numbers),
    path('student/', views.student_info),
]
