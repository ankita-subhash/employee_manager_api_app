
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('payment/', views.payment, name= "payment"),
    path('payment-status/', views.payment_status, name= "payment_status"),
    path('emp-list/', views.emp_list, name= 'emplist'),
    path('add-emp/', views.add_emp, name= 'add-emp'),
    path('update-emp/<int:id>/', views.update_emp, name= 'update-emp'),
    path('delete-emp/<int:id>/', views.delete_emp, name= 'delete-emp'),
    path('register/', views.Register, name= 'register'),
    path('login/', views.Login, name= 'login'),
    path('logout/', views.Logout, name= 'logout'),
    
]