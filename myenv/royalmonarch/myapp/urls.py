from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('knowledge/',views.knowledge, name='knowledge'),
    path('check_mail',views.check_mail)
]