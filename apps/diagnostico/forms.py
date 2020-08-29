from django import models
from  .models import diagnostico

class diagnosticoForm(forms.ModelForm):
    class Meta:
        model = diagnostico
        fields = ['nombre_diagnostico','descripcion_diagnostico']
