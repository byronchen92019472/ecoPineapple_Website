from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views import generic

from .models import Product

# Create your views here.


def home(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'home.html', context={ 'num_visits': num_visits})

#def product_homeXXXX(request):
#     # Number of visits to this view, as counted in the session variable.
#    num_visits=request.session.get('num_visits', 0)
#    request.session['num_visits'] = num_visits+1

#    return render(request, 'product_home.html', context={ 'num_visits': num_visits})

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

 
    

    
    
    
#def products(request):
#    return render(request,'product_home.html',{})
    
def product_list(request):
    products_list=Product.objects.all()
    return render(request,'product_list.html',{'products' :products_list})


#def product_detail(request):
#    product_details=Product.objects.all()
#    return render(request,'product_detail.html',{'products' :product_details})





#def product_detail(request, id):
#    obj=get_object_or_404(Product, id=id)
#    context={
#        "object":obj
#    }
#    return render(request, 'product_detail.html', context)
#    try:
#        product = Product.objects.get(id=id)
#    except Product.DoesNotExist:
#        raise Http404('Product not found')
#    return render(request, 'product_detail.html', {'id': id})



class ProductDetailView(generic.DetailView):
    template_name='product_detail.html'
    #queryset = Product

    #def get_object(self):
    #    id_=self.kwargs.get("id")
    #    return get_object_or_404(Product, id=id_)
    ##    return super().get_object(queryset)(id=id)
    model = Product










#def product_detail(request, primary_key):
#    try:
#        product = Product.objects.get(productid=primary_key)
#    except Book.DoesNotExist:
#        raise Http404('Book does not exist')
    
#    return render(request, 'product_detail.html', context={'product': product})
    
