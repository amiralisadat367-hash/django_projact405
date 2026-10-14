from django.urls import path
from .views import   Product_list , get_search

urlpatterns = [
    path('', Product_list.as_view()),
    # path('<int:pk>/', Product_details.as_view()),
    path('search/', get_search)
]