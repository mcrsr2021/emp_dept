from django.db import models
from django.urls.base import reverse

class Dept(models.Model):
    deptno = models.PositiveIntegerField(primary_key=True,unique=True)
    dname = models.CharField(max_length=255)
    loc = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.deptno}"

    def get_absolute_url(self):
        return reverse('dept_list')

class Emp(models.Model):
    empno = models.PositiveIntegerField(primary_key=True,unique=True)
    ename = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    mgr = models.PositiveIntegerField(null=True,blank=True)
    hiredate = models.DateField()
    sal = models.DecimalField(max_digits=7,decimal_places=2)
    comm = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    deptno = models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse('home')
