from django.forms import ModelForm
from .models import Ocean, Lake

class OceanForm(ModelForm):
    class Meta:
        model = Ocean
        fields ='__all__'
        
class LakeForm(ModelForm):
    class Meta:
        model = Lake
        fields ='__all__'