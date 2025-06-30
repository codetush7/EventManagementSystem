from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Event
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
            return redirect('welcome')  
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'myapp/customer.html')  
        
class BookEventView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'myapp/book.html')

    @method_decorator(login_required)
    def post(self, request):
        event_type = request.POST.get('event_type')
        event_date = request.POST.get('event_date')
        venue = request.POST.get('venue')
        guests = request.POST.get('guests')
        instructions = request.POST.get('instructions')

        event = Event.objects.create(
                    customer=request.user,
                    event_type=event_type,
                    event_date=event_date,
                    venue=venue,
                    guests=guests,
                    instructions=instructions,
                )

        # TODO: Save to your Event model (create if not exists)
        print("Saving event: ", event_type, event_date, venue, guests, instructions)

        # Optionally, store in session if needed later
        request.session['guestCount'] = guests

        return redirect('food')  # Must create this route  

def employee(request):
    return render(request,'myapp/employee.html')

def register(request):
    return render(request,'myapp/register.html')

def about_us(request):
    return render(request,'myapp/about.html')

def welcome(request):
    return render(request, 'myapp/welcome.html')

def bookevent(request):
    if request.method == "POST":
        request.session["event_type"] = request.POST.get("event_type")
        request.session["event_date"] = request.POST.get("event_date")
        request.session["venue"] = request.POST.get("venue")
        request.session["guestCount"] = request.POST.get("guests")
        request.session["instructions"] = request.POST.get("instructions")
        return redirect('food')  # your food menu page
    return render(request, 'myapp/book.html')

def food(request):
    return render(request, 'myapp/food.html')

def food_summary(request):
    return render(request, 'myapp/food-summary.html')

def venue(request):
    return render(request, 'myapp/venue.html')

def final_bill(request):
    return render(request, 'myapp/final-bill.html')
