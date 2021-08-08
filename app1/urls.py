from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('emp_create',views.EmpCreate.as_view(),name='emp_create'),
    path('emp_update/<int:pk>',views.EmpUpdate.as_view(),name='emp_update'),
    path('emp_delete/<int:pk>',views.EmpDelete.as_view(),name='emp_delete'),
    path('dept_create',views.DeptCreate.as_view(),name='dept_create'),
    path('dept_list',views.DeptList.as_view(),name='dept_list'),
    path('dept_update/<int:pk>',views.DeptUpdate.as_view(),name='dept_update'),
    path('dept_delete/<int:pk>',views.DeptDelete.as_view(),name='dept_delete'),
]