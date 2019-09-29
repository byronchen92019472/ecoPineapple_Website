from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#from home.forms import AgentDetailForm
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.views import generic




@login_required(login_url='/accounts/login/')
def home(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'home.html', context={ 'num_visits': num_visits})

 

# return agent details - should allow edits - not working see below
#def agent_detail(request, id):
#    try:
#        tour = Agent.objects.get(id=id)
#    except Agent.DoesNotExist:
#        raise Http404('Tour not found')
#    return render(request, 'agent_detail.html', {'agent': agent})


# add agent
#def add_agent(request):
#    if request.method=="POST":
#        form=AgentDetailForm(request.POST)

#edit agent
#def update_agent(request, id=None):
#    item=get_object_or_404(Agent,id=id)
#    form=AgentDetailForm(request.POST or None, instance=item)
#    if form.is_valid():
#        form.save()
#    return render(request, 'agent_detail.html', {'form':form})