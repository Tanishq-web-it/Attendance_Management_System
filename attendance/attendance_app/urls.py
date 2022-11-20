from django.urls import path
 
# importing views from views..py
from .views import update_view
from . import views

urlpatterns = [
    path('',views.student, name ='student'),
    path('teacherform/',views.teacherform, name ="teacherform"),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('<id>/update', update_view ),
    #path('add', views.add, name='add')
]