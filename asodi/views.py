from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import  Usuario, FichaPersonal, RegistroCitasMedicas, RegistroSintoma, RegistroPresion, RegistroPeso, Medicacion, RegistroMediTomado, Anuncios, UsuarioAsodi
from .serializer import  UsuarioSerializer, FichaPersonalSerializer, RegistroCitasMedicasSerializer, RegistroSintomaSerializer, RegistroPresionSerializer, RegistroPesoSerializer, MedicacionSerializer, RegistroMediTomadoSerializer, AnunciosSerializer, UsuarioAsodiSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, FichaPersonal, RegistroCitasMedicas, RegistroSintoma, RegistroPresion, RegistroPeso, Medicacion, RegistroMediTomado, Anuncios, UsuarioAsodi
from .serializer import UsuarioSerializer, FichaPersonalSerializer, RegistroCitasMedicasSerializer, RegistroSintomaSerializer, RegistroPresionSerializer, RegistroPesoSerializer, MedicacionSerializer, RegistroMediTomadoSerializer, AnunciosSerializer, UsuarioAsodiSerializer

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
    try:
        usuario = Usuario.objects.get(rut=rut)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

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
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def vista_ficha_personal(request, id_ficha):
    try:
        ficha = FichaPersonal.objects.get(id_ficha=id_ficha)
    except FichaPersonal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FichaPersonalSerializer(ficha)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = FichaPersonalSerializer(ficha, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
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

@api_view(['GET', 'PUT'])
def vista_registro_citas_medicas(request, id_cita_medica):
    try:
        cita = RegistroCitasMedicas.objects.get(id_cita_medica=id_cita_medica)
    except RegistroCitasMedicas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistroCitasMedicasSerializer(cita)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = RegistroCitasMedicasSerializer(cita, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
def vista_registro_sintoma(request, id_registro):
    try:
        sintoma = RegistroSintoma.objects.get(id_registro=id_registro)
    except RegistroSintoma.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistroSintomaSerializer(sintoma)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = RegistroSintomaSerializer(sintoma, data=data)
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

@api_view(['GET', 'PUT'])
def vista_registro_presion(request, id_presion):
    try:
        presion = RegistroPresion.objects.get(id_presion=id_presion)
    except RegistroPresion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistroPresionSerializer(presion)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = RegistroPresionSerializer(presion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET', 'PUT'])
def vista_registro_peso(request, id_peso):
    try:
        peso = RegistroPeso.objects.get(id_peso=id_peso)
    except RegistroPeso.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistroPesoSerializer(peso)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = RegistroPesoSerializer(peso, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET', 'PUT'])
def vista_medicacion(request, id_medicacion):
    try:
        medicacion = Medicacion.objects.get(id_medicacion=id_medicacion)
    except Medicacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MedicacionSerializer(medicacion)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = MedicacionSerializer(medicacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
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
def vista_registro_medi_tomado(request, id_registro_medi):
    try:
        registro = RegistroMediTomado.objects.get(id_registro_medi=id_registro_medi)
    except RegistroMediTomado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistroMediTomadoSerializer(registro)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = RegistroMediTomadoSerializer(registro, data=data)
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
    try:
        anuncio = Anuncios.objects.get(id_anuncio=id_anuncio)
    except Anuncios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

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
    try:
        usuario_asodi = UsuarioAsodi.objects.get(id_usuario=id_usuario)
    except UsuarioAsodi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

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

