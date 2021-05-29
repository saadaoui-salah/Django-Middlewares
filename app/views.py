from django.shortcuts import render
from .forms import PersonForm

class DemoException(Exception):
    pass

def simple_view(request):
    if request.method == 'POST':
        form = PersonForm()
        context = {
            'form' : form
        }
        raise DemoException('This is just a demo exce')
        
    return render(request, template_name="form.html", context=context )
