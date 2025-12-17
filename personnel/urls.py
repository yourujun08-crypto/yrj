# personnel/urls.py
from django.urls import path
from . import views



urlpatterns = [
    # 员工URL
    path('employees/', views.employees_list, name='employees_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/add/', views.employee_create, name='employee_create'),
    # path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'), # 编辑视图待实现

    # 请假URL
    path('leaves/', views.leaves_list, name='leaves_list'),
    path('leaves/<int:pk>/', views.leave_detail, name='leave_detail'),
    path('leaves/add/', views.leave_create, name='leave_create'),
    # path('leaves/<int:pk>/edit/', views.leave_update, name='leave_update'), # 编辑视图待实现
# 部门列表页：访问/departments/时触发departments_list视图
    path('departments/', views.departments_list, name='departments_list'),
    # 部门创建页（关键：添加此行）
    path('departments/add/', views.department_create, name='department_create'),
    # 其他URL（如详情页、编辑页等）可后续添加

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
