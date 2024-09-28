from rest_framework import serializers
from .models import (
    Usuario, 
    FichaPersonal, 
    RegistroCitasMedicas, 
    RegistroSintoma, 
    RegistroPresion, 
    RegistroPeso, 
    Anuncios, 
    UsuarioAsodiAdmin, 
    UsuarioAsodiAd, 
    Convenios, 
    PlanillasConvenio
)

# Serializer para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# Serializer para FichaPersonal
class FichaPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaPersonal
        fields = '__all__'

# Serializer para RegistroCitasMedicas
class RegistroCitasMedicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroCitasMedicas
        fields = '__all__'

# Serializer para RegistroSintoma
class RegistroSintomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroSintoma
        fields = '__all__'

# Serializer para RegistroPresion
class RegistroPresionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPresion
        fields = '__all__'

# Serializer para RegistroPeso
class RegistroPesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPeso
        fields = '__all__'

# Serializer para Anuncios
class AnunciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncios
        fields = '__all__'

# Serializer para UsuarioAsodiAdmin
class UsuarioAsodiAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAsodiAdmin
        fields = '__all__'

# Serializer para UsuarioAsodiAd
class UsuarioAsodiAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAsodiAd
        fields = '__all__'

# Serializer para Convenios
class ConveniosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenios
        fields = '__all__'

# Serializer para PlanillasConvenio
class PlanillasConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanillasConvenio
        fields = '__all__'
