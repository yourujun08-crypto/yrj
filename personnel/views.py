# personnel/views.py
from django.http import HttpResponse

def dashboard(request):
    """
    仪表盘视图原型
    """
    return HttpResponse("Welcome to the HRM system dashboard! This will display key statistics.")

def employee_list(request):
    """
    员工列表页视图原型
    """
    return HttpResponse("This is the employee list page, which will display all employees.")

def employee_detail(request, employee_id):
    """
    员工详情页视图原型
    :param employee_id: 从URL中捕获的员工ID
    """
    return HttpResponse(f"This is the employee detail page, displaying information for employee ID {employee_id}.")

def department_list(request):
    """
    部门列表页视图原型
    """
    return HttpResponse("This is the department list page, which will display all departments.")

def department_detail(request, department_id):
    """
    部门详情页视图原型
    :param department_id: 从URL中捕获的部门ID
    """
    return HttpResponse(f"This is the department detail page, displaying the department with ID {department_id} and its employees.")

def leave_list(request):
    """
    休假申请列表页视图原型
    """
    return HttpResponse("This is the leave request list page, for HR managers to view and process all requests.")

def leave_request(request):
    """
    创建休假申请页视图原型
    """
    return HttpResponse("This is the form page for creating a leave request.")

def leave_approve(request, leave_id):
    """
    审批休假操作视图原型
    :param leave_id: 从URL中捕获的休假申请ID
    """
    return HttpResponse(f"Operation successful: Leave request ID {leave_id} has been approved.")
