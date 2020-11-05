from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'), #eg: /polls/

    path('<int:question_id>/', views.detail, name='detail') #eg: /polls/5/

    
]
