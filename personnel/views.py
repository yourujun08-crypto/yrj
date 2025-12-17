# personnel/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Department  # 导入Department模型（需确保模型已创建）
from .models import Employee, Leave
from .forms import EmployeeForm, LeaveForm, DepartmentForm
from django.shortcuts import get_object_or_404, redirect

# --- 员工视图 ---
def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'personnel/employees_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'personnel/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_list')
    else:
        form = EmployeeForm()
    return render(request, 'personnel/employee_form.html', {'form': form})

# --- 请假视图 ---
def leaves_list(request):
    leaves = Leave.objects.all()
    return render(request, 'personnel/leaves_list.html', {'leaves': leaves})

def leave_detail(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    return render(request, 'personnel/leave_detail.html', {'leave': leave})

def leave_create(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leaves_list')
    else:
        form = LeaveForm()
    return render(request, 'personnel/leave_form.html', {'form': form})

def department_create(request):
    """
    创建新部门的视图
    """
    if request.method == 'POST':
        # 处理POST请求（表单提交）
        form = DepartmentForm(request.POST)  # 获取表单数据
        if form.is_valid():
            form.save()  # 保存到数据库
            return redirect('departments_list')  # 重定向到部门列表页
    else:
        # 处理GET请求（显示空表单）
        form = DepartmentForm()
    # 渲染表单页面（department_form.html）
    return render(request, 'personnel/department_form.html', {'form': form})

def departments_list(request):
    """
    视图功能：从数据库获取所有部门，传递给模板显示
    """
    # 1. 从数据库获取所有部门对象（QuerySet，类似Python列表）
    departments = Department.objects.all()

    # 2. 将departments传递给模板（模板中用'departments'变量访问）
    # render的第三个参数是字典，键为模板变量名，值为传递的数据
    return render(request, 'personnel/departments_list.html', {'departments': departments})
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
