from rest_framework import serializers
from .models import Usuario, FichaPersonal, RegistroCitasMedicas, RegistroSintoma, RegistroPresion, RegistroPeso, Medicacion, RegistroMediTomado, Anuncios, UsuarioAsodi

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # Incluye todos los campos del modelo en la representación del serializador
       
class FichaPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaPersonal
        fields = '__all__'

class RegistroCitasMedicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroCitasMedicas
        fields = '__all__'

class RegistroSintomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroSintoma
        fields = '__all__'

class RegistroPresionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPresion
        fields = '__all__'

class RegistroPesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPeso
        fields = '__all__'

class MedicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicacion
        fields = '__all__'

class RegistroMediTomadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroMediTomado
        fields = '__all__'

class AnunciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncios
        fields = '__all__'

class UsuarioAsodiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAsodi
        fields = '__all__'  # Incluye todos los campos del modelo en la representación del serializador
        extra_kwargs = {
            'password': {'write_only': True}  # La contraseña solo debe ser escrita
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Extrae la contraseña
        usuario = UsuarioAsodi.objects.create(**validated_data)  # Crea el usuario
        if password:
            usuario.set_password(password)  # Encripta la contraseña
        usuario.save()  # Guarda el usuario
        return usuario
