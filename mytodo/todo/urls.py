from django.urls import path
from todo.views import hello, updatetodo, delettodo, deletconfirmation

urlpatterns = [
    path('',hello,name='hello'),
    path('updatetodo/<str:pk>/',updatetodo,name='updatetodo'),
    path('delettodo/<str:pk>/',delettodo,name='delettodo'),
    path('deletconfirmation/<str:pk>/',deletconfirmation,name='deletconfirmation'),
]