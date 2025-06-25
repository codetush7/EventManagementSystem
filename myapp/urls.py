from django.urls import path
from . import views
from .views import CustomerLoginView
from .views import CustomerRegisterView

urlpatterns = [
    path("",views.index,name='index'),
    path("register/",CustomerRegisterView.as_view(), name="register"),
    path("customer/",CustomerLoginView.as_view(),name='customer'),
    path("employee/",views.employee,name='employee'),
    path("register/",views.register,name='register'),
    path("about_us/",views.about_us,name='about_us'),

]
