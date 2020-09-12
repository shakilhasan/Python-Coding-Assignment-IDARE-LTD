from django.shortcuts import render
from .models import Pipe
from .forms import PipeForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    template = loader.get_template('pipe/home.html')
    form = PipeForm
    context = {'form':form}
    return HttpResponse(template.render(context, request))

def result(request):
    template = loader.get_template('pipe/result.html')
    if request.method == 'POST':
        form = PipeForm(request.POST)
        if form.is_valid():
            instance=form.save()
    #pipe = Pipe.objects.get(id=instance.id)
    context = {'pipe': instance}
    return HttpResponse(template.render(context, request))
