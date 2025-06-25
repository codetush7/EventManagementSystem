from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from .models import Customer
# Create your views here.

def index(request):
    return render(request,'myapp/index.html')
class CustomerRegisterView(View):
    def get(self, request):
        return render(request, 'myapp/register.html')

    def post(self, request):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('date_of_birth')
        password = request.POST.get('password')

        # Create User
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create Customer profile
        Customer.objects.create(user=user, mobile=mobile, date_of_birth=dob)

        return redirect('customer')  # Login page 
class CustomerLoginView(View):
    def get(self, request):
        return render(request, 'myapp/customer.html')
    def post(self, request):
        email = request.POST.get('email_or_id')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return HttpResponse("You have successfully logged in ") 
        else:
            messages.error(request, "Invalid credentials")
            return HttpResponse("Not a valid user")

def employee(request):
    return render(request,'myapp/employee.html')

def register(request):
    return render(request,'myapp/register.html')

def about_us(request):
    return render(request,'myapp/about.html')