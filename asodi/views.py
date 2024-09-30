from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import (
    Convenios, PlanillasConvenio, Solicitudes, Usuario, FichaPersonal, RegistroCitasMedicas, RegistroSintoma,
    RegistroPresion, RegistroPeso,
    Anuncios,  UsuarioAsodiAd, UsuarioAsodiAdmin
)
from .serializer import (
    ConveniosSerializer, PlanillasConvenioSerializer, SolicitudesSerializer, UsuarioAsodiAdSerializer, UsuarioAsodiAdminSerializer, UsuarioSerializer, FichaPersonalSerializer, RegistroCitasMedicasSerializer,
    RegistroSintomaSerializer, RegistroPresionSerializer, RegistroPesoSerializer,
    AnunciosSerializer
)

@api_view(['GET', 'POST'])
def listado_usuario(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def vista_usuario(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def listado_ficha_personal(request):
    if request.method == 'GET':
        fichas = FichaPersonal.objects.all()
        serializer = FichaPersonalSerializer(fichas, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = FichaPersonalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def vista_ficha_personal(request, rut):
    ficha = get_object_or_404(FichaPersonal, usuario__rut=rut)  # Usamos el rut como clave primaria
    if request.method == 'GET':
        serializer = FichaPersonalSerializer(ficha)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FichaPersonalSerializer(ficha, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def listado_registro_citas_medicas(request):
    if request.method == 'GET':
        citas = RegistroCitasMedicas.objects.all()
        serializer = RegistroCitasMedicasSerializer(citas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = RegistroCitasMedicasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vista_registro_citas_medicas(request, rut, id=None):
    usuario = get_object_or_404(Usuario, rut=rut)
    citas = RegistroCitasMedicas.objects.filter(usuario=usuario)

    if request.method == 'GET':
        serializer = RegistroCitasMedicasSerializer(citas, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        cita = get_object_or_404(RegistroCitasMedicas, id_cita_medica=id, usuario=usuario)
        serializer = RegistroCitasMedicasSerializer(cita, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cita = get_object_or_404(RegistroCitasMedicas, id_cita_medica=id, usuario=usuario)
        cita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def listado_registro_sintoma(request):
    if request.method == 'GET':
        sintomas = RegistroSintoma.objects.all()
        serializer = RegistroSintomaSerializer(sintomas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = RegistroSintomaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def vista_registro_sintoma(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    sintomas = RegistroSintoma.objects.filter(usuario=usuario)
    
    if request.method == 'GET':
        serializer = RegistroSintomaSerializer(sintomas, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = RegistroSintomaSerializer(sintomas.first(), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def listado_registro_presion(request):
    if request.method == 'GET':
        presiones = RegistroPresion.objects.all()
        serializer = RegistroPresionSerializer(presiones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = RegistroPresionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vista_registro_presion(request, rut, id=None):
    usuario = get_object_or_404(Usuario, rut=rut)
    presiones = RegistroPresion.objects.filter(usuario=usuario)

    if request.method == 'GET':
        serializer = RegistroPresionSerializer(presiones, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        presion = get_object_or_404(RegistroPresion, id_presion=id, usuario=usuario)
        serializer = RegistroPresionSerializer(presion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        presion = get_object_or_404(RegistroPresion, id_presion=id, usuario=usuario)
        presion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def listado_registro_peso(request):
    if request.method == 'GET':
        pesos = RegistroPeso.objects.all()
        serializer = RegistroPesoSerializer(pesos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = RegistroPesoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vista_registro_peso(request, rut, id=None):
    usuario = get_object_or_404(Usuario, rut=rut)
    pesos = RegistroPeso.objects.filter(usuario=usuario)

    if request.method == 'GET':
        serializer = RegistroPesoSerializer(pesos, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        peso = get_object_or_404(RegistroPeso, id_peso=id, usuario=usuario)
        serializer = RegistroPesoSerializer(peso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        peso = get_object_or_404(RegistroPeso, id_peso=id, usuario=usuario)
        peso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def listado_anuncios(request):
    if request.method == 'GET':
        anuncios = Anuncios.objects.all()
        serializer = AnunciosSerializer(anuncios, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data.copy()  # Hacemos una copia de los datos para no modificar el original
        files = request.FILES.get('imagen')  # Extraemos la imagen de los archivos
        serializer = AnunciosSerializer(data=data, files=request.FILES)  # Asegúrate de pasar los archivos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def vista_anuncios(request, id_anuncio):
    anuncio = get_object_or_404(Anuncios, id_anuncio=id_anuncio)
    
    if request.method == 'GET':
        serializer = AnunciosSerializer(anuncio)
        return Response(serializer.data)
    
    elif request.method in ['PUT', 'PATCH']:
        data = request.data.copy()
        files = request.FILES.get('imagen')
        serializer = AnunciosSerializer(anuncio, data=data, files=request.FILES, partial=(request.method == 'PATCH'))
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        anuncio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def listado_usuario_asodi_admin(request):
    if request.method == 'GET':
        usuarios_asodi_admin = UsuarioAsodiAdmin.objects.all()
        serializer = UsuarioAsodiAdminSerializer(usuarios_asodi_admin, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = UsuarioAsodiAdminSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def vista_usuario_asodi_admin(request, correo):
    usuario_asodi_admin = get_object_or_404(UsuarioAsodiAdmin, correo=correo)
    if request.method == 'GET':
        serializer = UsuarioAsodiAdminSerializer(usuario_asodi_admin)
        return Response(serializer.data)
    


@api_view(['GET', 'POST'])
def listado_usuario_asodi_ad(request):
    if request.method == 'GET':
        usuarios_asodi_ad = UsuarioAsodiAd.objects.all()
        serializer = UsuarioAsodiAdSerializer(usuarios_asodi_ad, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = UsuarioAsodiAdSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vista_usuario_asodi_ad(request, rut_ad):
    usuario_asodi_ad = get_object_or_404(UsuarioAsodiAd, rut_ad=rut_ad)
    if request.method == 'GET':
        serializer = UsuarioAsodiAdSerializer(usuario_asodi_ad)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UsuarioAsodiAdSerializer(usuario_asodi_ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario_asodi_ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def listado_convenios(request):
    if request.method == 'GET':
        convenios = Convenios.objects.all()
        serializer = ConveniosSerializer(convenios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = ConveniosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vista_convenios(request, id_convenio):
    convenio = get_object_or_404(Convenios, id_convenio=id_convenio)
    if request.method == 'GET':
        serializer = ConveniosSerializer(convenio)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ConveniosSerializer(convenio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        convenio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def listado_planillas_convenio(request):
    if request.method == 'GET':
        planillas = PlanillasConvenio.objects.all()
        serializer = PlanillasConvenioSerializer(planillas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PlanillasConvenioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vista_planillas_convenio(request, id_planilla):
    planilla = get_object_or_404(PlanillasConvenio, id_planilla=id_planilla)
    if request.method == 'GET':
        serializer = PlanillasConvenioSerializer(planilla)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PlanillasConvenioSerializer(planilla, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        planilla.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def listado_solicitudes(request):
    if request.method == 'GET':
        solicitudes = Solicitudes.objects.all()
        serializer = SolicitudesSerializer(solicitudes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = SolicitudesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vista_solicitud(request, id_soli):
    solicitud = get_object_or_404(Solicitudes, id_soli=id_soli)
    
    if request.method == 'GET':
        serializer = SolicitudesSerializer(solicitud)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SolicitudesSerializer(solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)