from django.shortcuts import render
from django.http import HttpResponse
from .models import Depaertments,Doctors
from .form import BookingForm
a={"num":["hello","dennis", "joseph"]}

def home(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request, "booking.html", dict_form)
def contact(request):
    return render(request, "contact.html")
def doctors(request):
    dict_docs = {
        'dept': Doctors.objects.all()
    }
    return render(request, "doctors.html", dict_docs)
def departments(request):
    dict_dept = {
        'dept': Depaertments.objects.all()
    }
    return render(request, "departments.html", dict_dept)


