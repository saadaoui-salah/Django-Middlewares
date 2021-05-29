from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        models = Person
        fields = '__all__'
