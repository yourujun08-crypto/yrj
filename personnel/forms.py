# personnel/forms.py
from django import forms
from .models import Employee, Leave, Department


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'  # 或者指定 ['name', 'email', ...]
        fields = '__all__'

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'
# personnel/forms.py

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']  # 或 '__all__'（包含所有字段）
