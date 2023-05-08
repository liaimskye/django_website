from django.forms import ModelForm
from inventory.models import Query

class QueryForm(ModelForm):
    
    class Meta:
        model = Query
        fields = '__all__'

