from django.contrib import admin

from .models import diagnostico
from .models import experto
from .models import especialidad

admin.site.register(diagnostico)
admin.site.register(experto)
admin.site.register(especialidad)