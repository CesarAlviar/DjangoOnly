from rest_framework import serializers
from centidev.models import Post
from centidevNew.models import Report
from django.conf import settings


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('co_codigo', 'co_estatus', 'co_usuario', 'fe_update', 'co_empresa', 'tx_marca_empresa', 'co_opcion',
        'co_existe_modulo', 'nb_modulo_si', 'nb_modulo_no', 'co_tabla', 'co_database', 'co_grupo',
        'co_modulo', 'nb_opcion', 'co_tabla_nueva', 'co_tabla_temporal', 'nu_orden', 'co_lista', 'nu_orden_opcion', 'nb_tabla_centipede', 
        'co_visible', 'co_main', 'tx_tipo_opcion', 'co_search', 'tx_tipo_search', 'tx_procedure', 'tx_query', 'tx_type_output', 
        'co_output', 'tx_prefijo_export', 'nb_search',
        
        'category', 'id', 'title', 'slug', 'author', 'excerpt', 'content', 'status')

class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}

class  ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('co_codigo', 'co_estatus', 'co_usuario', 'fe_update', 'co_empresa', 'tx_marca_empresa', 'co_opcion',
        'co_existe_modulo', 'nb_modulo_si', 'nb_modulo_no', 'co_tabla', 'co_database', 'co_grupo',
        'co_modulo', 'nb_opcion', 'co_tabla_nueva', 'co_tabla_temporal', 'nu_orden', 'co_lista', 'nu_orden_opcion', 'nb_tabla_centipede', 
        'co_visible', 'co_main', 'tx_tipo_opcion', 'co_search', 'tx_tipo_search', 'tx_procedure', 'tx_query', 'tx_type_output', 
        'co_output', 'tx_prefijo_export', 'nb_search')