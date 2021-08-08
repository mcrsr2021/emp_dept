from app1.models import Emp,Dept
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class Home(ListView):
    model = Emp

class EmpCreate(CreateView):
    model = Emp
    fields = '__all__'

class EmpUpdate(UpdateView):
    model = Emp
    fields = '__all__'

class EmpDelete(DeleteView):
    model = Emp
    success_url = reverse_lazy('home')


class DeptCreate(CreateView):
    model = Dept
    fields = '__all__'

class DeptList(ListView):
    model = Dept


class DeptUpdate(UpdateView):
    model = Dept
    fields = '__all__'

class DeptDelete(DeleteView):
    model = Dept
    success_url = reverse_lazy('dept_list')
