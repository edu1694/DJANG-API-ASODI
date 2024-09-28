from django.contrib import admin
from .models import (
    Usuario, FichaPersonal, RegistroCitasMedicas, RegistroSintoma, 
    RegistroPresion, RegistroPeso, Anuncios, UsuarioAsodiAd, 
    Convenios, PlanillasConvenio, UsuarioAsodiAdmin
)

# Register your models here.
admin.site.register(Usuario)
admin.site.register(FichaPersonal)
admin.site.register(RegistroCitasMedicas)
admin.site.register(RegistroSintoma)
admin.site.register(RegistroPresion)
admin.site.register(RegistroPeso)
admin.site.register(Anuncios)
admin.site.register(UsuarioAsodiAd)
admin.site.register(Convenios)          
admin.site.register(PlanillasConvenio)   
admin.site.register(UsuarioAsodiAdmin)   
