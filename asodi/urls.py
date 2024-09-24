from django.urls import path
from . import views

urlpatterns = [
    # URLs para Usuario
    path('v1/usuarios/', views.listado_usuario, name='listado_usuario'),
    path('v1/usuarios/<rut>/', views.vista_usuario, name='vista_usuario'),

    # URLs para FichaPersonal
    path('v1/fichas/', views.listado_ficha_personal, name='listado_ficha_personal'),
    path('v1/fichas/<rut>/', views.vista_ficha_personal, name='vista_ficha_personal'),

    # URLs para RegistroCitasMedicas
    path('v1/citas/', views.listado_registro_citas_medicas, name='listado_registro_citas_medicas'),
    path('v1/citas/<rut>/', views.vista_registro_citas_medicas, name='vista_registro_citas_medicas'),
    path('v1/citas/<rut>/<int:id>/', views.vista_registro_citas_medicas, name='detalle_registro_citas_medicas'),

    # URLs para RegistroSintoma
    path('v1/sintomas/', views.listado_registro_sintoma, name='listado_registro_sintoma'),
    path('v1/sintomas/<rut>/', views.vista_registro_sintoma, name='vista_registro_sintoma'),

    # URLs para RegistroPresion
    path('v1/presiones/', views.listado_registro_presion, name='listado_registro_presion'),
    path('v1/presiones/<rut>/', views.vista_registro_presion, name='vista_registro_presion'),
    path('v1/presiones/<rut>/<int:id>/', views.vista_registro_presion, name='detalle_registro_presion'),

    # URLs para RegistroPeso
    path('v1/pesos/', views.listado_registro_peso, name='listado_registro_peso'),
    path('v1/pesos/<rut>/', views.vista_registro_peso, name='vista_registro_peso'),
    path('v1/pesos/<rut>/<int:id>/', views.vista_registro_peso, name='detalle_registro_peso'),

    # URLs para Anuncios
    path('v1/anuncios/', views.listado_anuncios, name='listado_anuncios'),
    path('v1/anuncios/<int:id_anuncio>/', views.vista_anuncios, name='vista_anuncios'),

    # URLs para UsuarioAsodi
    path('v1/usuarios-asodi/', views.listado_usuario_asodi, name='listado_usuario_asodi'),
    path('v1/usuarios-asodi/<int:id_usuario>/', views.vista_usuario_asodi, name='vista_usuario_asodi'),
]
