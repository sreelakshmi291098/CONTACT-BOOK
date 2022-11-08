from django.urls import path
from app17 import views
urlpatterns=[
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('addcontact',views.saveinfo,name='addcontact'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('search',views.search,name='search'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('<int:id>/formupdate',views.formupdate,name='formupdate'),
]
