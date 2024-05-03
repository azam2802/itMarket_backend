from django.urls import path,include
from .views import *

urlpatterns = [
    path('products/',ProductApi.as_view()),
    path('products/<int:pk>',ProductDetail.as_view()),

    path('categories/',CategoryApi.as_view()),
    path('categories/<int:pk>',CategoryDetail.as_view())
]
