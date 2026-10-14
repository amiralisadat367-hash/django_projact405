from django.urls import path
from .views import  *

urlpatterns = [
    path('', Accont_list.as_view()),
    path('<int:pk>/', Accont_details.as_view()),
]