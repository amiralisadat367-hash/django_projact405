from django.urls import path
from .views import   Product_list , get_search,Product_Retrieve

urlpatterns = [
    path('', Product_list.as_view()),
    path('<int:pk>/', Product_Retrieve.as_view()),
    path('search/', get_search)
]