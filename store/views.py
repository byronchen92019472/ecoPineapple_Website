from django.shortcuts import render
from .models import Product


# Create your views here.


def home(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'home.html', context={ 'num_visits': num_visits})

def product_homeXXXX(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'product_home.html', context={ 'num_visits': num_visits})

def about(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'about.html', context={ 'num_visits': num_visits})

def contact(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'contact.html', context={ 'num_visits': num_visits})

def rocket(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'rocket_home.html', context={ 'num_visits': num_visits})

def staff_list(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'staff_list.html', context={ 'num_visits': num_visits})

def login(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'login.html', context={ 'num_visits': num_visits})    
    
def logout(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'login.html', context={ 'num_visits': num_visits})  
    
    
    
#def products(request):
#    return render(request,'product_home.html',{})
    
def product_home(request):
    products_list=Product.objects.all()
    return render(request,'product_home.html',{'products' :products_list})


def product_detail(request):
    product_details=Product.objects.all()
    return render(request,'product_detail.html',{'products' :product_details})
    


#def tour_detail(request, id):
#    try:
#        tour = Tour.objects.get(id=id)
#    except Tour.DoesNotExist:
#        raise Http404('Tour not found')
#    return render(request, 'tour_detail.html', {'tour': tour})


#class TourDetailView(LoginRequiredMixin,generic.DetailView):
#    model = Product