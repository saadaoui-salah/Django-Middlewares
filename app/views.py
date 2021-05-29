from django.shortcuts import render
from .forms import PersonForm

class DemoException(Exception):
    pass

def simple_view(request):
    form = PersonForm()
    context = {
        'form' : form
    }
    raise DemoException('this just exception test for middleware')
    return render(request, template_name="form.html", context=context )
