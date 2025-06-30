from django.urls import path
from . import views
from .views import CustomerLoginView
from .views import CustomerRegisterView,BookEventView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",views.index,name='index'),
    path("register/",CustomerRegisterView.as_view(), name="register"),
    path("customer/",CustomerLoginView.as_view(),name='customer'),
    path("employee/",views.employee,name='employee'),
    path("about_us/",views.about_us,name='about_us'),
    path("welcome/",views.welcome,name='welcome'),
    path("bookevent/",BookEventView.as_view(),name='bookevent'),
    path('logout/', LogoutView.as_view(next_page='customer'), name='logout'),
    path('food/', views.food, name='food'),
    path('food-summary/', views.food_summary, name='food_summary'),
    path('venue/', views.venue, name='venue'),
    path('final-bill/', views.final_bill, name='final_bill'),
  


]
