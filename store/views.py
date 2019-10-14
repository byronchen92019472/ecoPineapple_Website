from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views import generic

from .models import Product
from .models import Profile

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

def rocket_list(request):
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'rocket_list.html', context={ 'num_visits': num_visits})


def staff_detailtest(request):

    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'staff_detailtest.html', context={ 'num_visits': num_visits}) 



def product_list(request):
    products_list=Product.objects.all()
    return render(request,'product_list.html',{'products' :products_list})

class ProductDetailView(generic.DetailView):
    template_name='product_detail.html'
    model = Product



@login_required
def profile_list(request):
    profiles_list=Profile.objects.all()
    return render(request,'profile_list.html',{'profiles' :profiles_list})


class ProfileDetailView(generic.DetailView):
    template_name='profile_detail.html'
    model = Profile

