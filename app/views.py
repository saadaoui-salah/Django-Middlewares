from django.shortcuts import render
from .forms import PersonForm

class DemoException(Exception):
    pass

def simple_view(request):
    form = PersonForm()
    context = {
        'form' : form
    }
    return render(request, template_name="form.html", context=context )
