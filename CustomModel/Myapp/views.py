from django.shortcuts import render,HttpResponse
from .models import Student,ProxyStudents
# Create your views here.

def student_info(request):
#     student_1=ProxyStudents.stu.get_stu_age_range(20,24)  #customModel objects
    student_1=ProxyStudents.stu.get_stu_age_range(21,23) #defaultModel objects

    context={
          'students':student_1
    }

    return render(request,'student.html',context)
