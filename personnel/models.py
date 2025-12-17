from django.db import models


# 部门模型：存储部门信息
class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Department Name")
    description = models.TextField(blank=True, null=True, verbose_name="Department Description")

    def __str__(self):
        return self.name  # 在管理后台显示部门名称

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Department List"


# 员工模型：存储员工信息，关联部门
class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="Employee Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,  # 部门删除时，员工记录也删除
        related_name="employees",  # 反向关联名称（可通过部门.employees访问员工）
        verbose_name="Department"
    )
    position = models.CharField(max_length=100, verbose_name="Position")
    hire_date = models.DateField(verbose_name="Hire Date")

    def __str__(self):
        return self.name  # 在管理后台显示员工姓名

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee List"


# 请假模型：存储请假申请，关联员工
class Leave(models.Model):
    # 请假类型选项（choices用于下拉菜单）
    LEAVE_TYPES = (
        ('annual', 'Annual Leave'),
        ('sick', 'Sick Leave'),
        ('personal', 'Personal Leave'),
    )
    # 请假状态选项
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,  # 员工删除时，请假记录也删除
        related_name="leaves",  # 反向关联名称（可通过员工.leaves访问请假记录）
        verbose_name="Employee"
    )
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    leave_type = models.CharField(
        max_length=20,
        choices=LEAVE_TYPES,
        verbose_name="Leave Type"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',  # 默认状态为“申请中”
        verbose_name="Status"
    )
    reason = models.TextField(blank=True, null=True, verbose_name="Reason")

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type} ({self.status})"  # 在管理后台显示可读信息

    class Meta:
        verbose_name = "Leave Application"
        verbose_name_plural = "Leave Application List"
        ordering = ['-start_date']  # 按开始日期降序排列（最新申请在前）
