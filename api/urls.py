from django.urls import path, include
from . import views

urlpatterns = [
    path('emp/', views.emplist ),
    path('emp/<int:pk>/',views.empview ),
    path('updateemp/<int:pk>/',views.updateemp),
    path('deleteemp/<int:pk>/',views.deleteemp),
    path('addemp/',views.addemp ),
    ]
