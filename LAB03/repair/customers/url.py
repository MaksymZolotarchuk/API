from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('<int:id>/', views.customer_detail, name='customer_detail'),
    path('add/', views.customer_add, name='customer_add'),
    path('delete/<int:id>/', views.customer_delete, name='customer_delete'),
    path('edit/<int:id>/', views.customer_edit, name='customer_edit'),
]
