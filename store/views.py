from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views import generic

from .models import Product, Rocket, Profile

# Create your views here.


def home(request):
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'home.html', context={ 'num_visits': num_visits})

def about(request):
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'about.html', context={ 'num_visits': num_visits})

def contact(request):
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'contact.html', context={ 'num_visits': num_visits})

def rocket_home(request):
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'rocket_home.html', context={ 'num_visits': num_visits})




#These views access data - product, rockets and staff(profile)
def product_list(request):
    products_list=Product.objects.all()
    return render(request,'product_list.html',{'products' :products_list})

class ProductDetailView(generic.DetailView):
    template_name='product_detail.html'
    model = Product


def rocket_list(request):
    rockets_list=Rocket.objects.all()
    return render(request,'rocket_list.html',{'rockets' :rockets_list})

class RocketDetailView(generic.DetailView):
    template_name='rocket_detail.html'
    model = Rocket




#These views are securered from view if not logged in
@login_required
def profile_list(request):
    profiles_list=Profile.objects.all()
    return render(request,'profile_list.html',{'profiles' :profiles_list})


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    template_name='profile_detail.html'
    model = Profile

