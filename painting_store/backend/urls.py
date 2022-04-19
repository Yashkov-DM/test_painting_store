from django.urls import path
from .views import StoreView

urlpatterns = [
    path('stores/', StoreView.as_view()),
    path('stores/<int:pk>/', StoreView.as_view()),
]