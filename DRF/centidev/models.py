from django.db import models
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='centidev_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    co_codigo = models.CharField(db_column='Co_Codigo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_estatus = models.CharField(db_column='Co_Estatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co_usuario = models.CharField(db_column='Co_Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fe_update = models.CharField(db_column='Fe_Update', default=timezone.now, max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_empresa = models.CharField(db_column='Co_Empresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tx_marca_empresa = models.CharField(db_column='Tx_Marca_Empresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_opcion = models.CharField(db_column='CO_OPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_existe_modulo = models.CharField(db_column='CO_EXISTE_MODULO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nb_modulo_si = models.CharField(db_column='NB_MODULO_SI', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nb_modulo_no = models.CharField(db_column='NB_MODULO_NO', max_length=250, blank=True, null=True)  # Field name made lowercase.
    co_tabla = models.CharField(db_column='CO_TABLA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_database = models.CharField(db_column='CO_DATABASE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    co_grupo = models.CharField(db_column='CO_GRUPO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    co_modulo = models.CharField(db_column='CO_MODULO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nb_opcion = models.CharField(db_column='NB_OPCION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    co_tabla_nueva = models.CharField(db_column='CO_TABLA_NUEVA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    co_tabla_temporal = models.CharField(db_column='CO_TABLA_TEMPORAL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nu_orden = models.FloatField(db_column='NU_ORDEN', blank=True, null=True)  # Field name made lowercase.
    co_lista = models.CharField(db_column='CO_LISTA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nu_orden_opcion = models.FloatField(db_column='NU_ORDEN_OPCION', blank=True, null=True)  # Field name made lowercase.
    nb_tabla_centipede = models.CharField(db_column='NB_TABLA_CENTIPEDE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_visible = models.CharField(db_column='CO_VISIBLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_main = models.CharField(db_column='CO_MAIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tx_tipo_opcion = models.CharField(db_column='TX_TIPO_OPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_search = models.CharField(db_column='CO_SEARCH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tx_tipo_search = models.CharField(db_column='TX_TIPO_SEARCH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tx_procedure = models.CharField(db_column='Tx_PROCEDURE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tx_query = models.CharField(db_column='Tx_QUERY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tx_type_output = models.CharField(db_column='TX_TYPE_OUTPUT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_output = models.CharField(db_column='CO_OUTPUT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tx_prefijo_export = models.CharField(db_column='TX_PREFIJO_EXPORT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nb_search = models.CharField(db_column='NB_SEARCH', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


