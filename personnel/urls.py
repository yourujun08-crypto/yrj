# personnel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 仪表盘
    path('', views.dashboard, name='dashboard'),

    # 员工相关路由
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),

    # 部门相关路由
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:department_id>/', views.department_detail, name='department_detail'),

    # 休假相关路由
    path('leaves/', views.leave_list, name='leave_list'),
    path('leaves/request/', views.leave_request, name='leave_request'),
    path('leaves/<int:leave_id>/approve/', views.leave_approve, name='leave_approve'),
]
