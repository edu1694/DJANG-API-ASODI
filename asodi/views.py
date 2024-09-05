from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import (
    Usuario, FichaPersonal, RegistroCitasMedicas, RegistroSintoma,
    RegistroPresion, RegistroPeso, Medicacion, RegistroMediTomado,
    Anuncios, UsuarioAsodi
)
from .serializer import (
    UsuarioSerializer, FichaPersonalSerializer, RegistroCitasMedicasSerializer,
    RegistroSintomaSerializer, RegistroPresionSerializer, RegistroPesoSerializer,
    MedicacionSerializer, RegistroMediTomadoSerializer, AnunciosSerializer,
    UsuarioAsodiSerializer
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
def listado_medicacion(request):
    if request.method == 'GET':
        medicaciones = Medicacion.objects.all()
        serializer = MedicacionSerializer(medicaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = MedicacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vista_medicacion(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    medicaciones = Medicacion.objects.filter(usuario=usuario)
    
    if request.method == 'GET':
        serializer = MedicacionSerializer(medicaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = MedicacionSerializer(medicaciones.first(), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        medicacion = medicaciones.first()
        medicacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def listado_registro_medi_tomado(request):
    if request.method == 'GET':
        registros = RegistroMediTomado.objects.all()
        serializer = RegistroMediTomadoSerializer(registros, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = RegistroMediTomadoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def vista_registro_medi_tomado(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    registros = RegistroMediTomado.objects.filter(medicacion__usuario=usuario)
    
    if request.method == 'GET':
        serializer = RegistroMediTomadoSerializer(registros, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = RegistroMediTomadoSerializer(registros.first(), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def listado_anuncios(request):
    if request.method == 'GET':
        anuncios = Anuncios.objects.all()
        serializer = AnunciosSerializer(anuncios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = AnunciosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def vista_anuncios(request, id_anuncio):
    anuncio = get_object_or_404(Anuncios, id_anuncio=id_anuncio)
    if request.method == 'GET':
        serializer = AnunciosSerializer(anuncio)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = AnunciosSerializer(anuncio, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def listado_usuario_asodi(request):
    if request.method == 'GET':
        usuarios_asodi = UsuarioAsodi.objects.all()
        serializer = UsuarioAsodiSerializer(usuarios_asodi, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = UsuarioAsodiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def vista_usuario_asodi(request, id_usuario):
    usuario_asodi = get_object_or_404(UsuarioAsodi, id_usuario=id_usuario)
    if request.method == 'GET':
        serializer = UsuarioAsodiSerializer(usuario_asodi)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = UsuarioAsodiSerializer(usuario_asodi, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
