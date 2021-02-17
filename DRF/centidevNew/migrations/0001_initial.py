# Generated by Django 3.0.1 on 2021-02-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TCentipanelMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_codigo', models.CharField(blank=True, db_column='Co_Codigo', max_length=50, null=True)),
                ('co_estatus', models.CharField(blank=True, db_column='Co_Estatus', max_length=20, null=True)),
                ('co_usuario', models.CharField(blank=True, db_column='Co_Usuario', max_length=50, null=True)),
                ('fe_update', models.CharField(blank=True, db_column='Fe_Update', max_length=50, null=True)),
                ('co_empresa', models.CharField(blank=True, db_column='Co_Empresa', max_length=50, null=True)),
                ('tx_marca_empresa', models.CharField(blank=True, db_column='Tx_Marca_Empresa', max_length=50, null=True)),
                ('co_opcion', models.CharField(blank=True, db_column='CO_OPCION', max_length=50, null=True)),
                ('co_existe_modulo', models.CharField(blank=True, db_column='CO_EXISTE_MODULO', max_length=50, null=True)),
                ('nb_modulo_si', models.CharField(blank=True, db_column='NB_MODULO_SI', max_length=250, null=True)),
                ('nb_modulo_no', models.CharField(blank=True, db_column='NB_MODULO_NO', max_length=250, null=True)),
                ('co_tabla', models.CharField(blank=True, db_column='CO_TABLA', max_length=50, null=True)),
                ('co_database', models.CharField(blank=True, db_column='CO_DATABASE', max_length=100, null=True)),
                ('co_grupo', models.CharField(blank=True, db_column='CO_GRUPO', max_length=100, null=True)),
                ('co_modulo', models.CharField(blank=True, db_column='CO_MODULO', max_length=50, null=True)),
                ('nb_opcion', models.CharField(blank=True, db_column='NB_OPCION', max_length=250, null=True)),
                ('co_tabla_nueva', models.CharField(blank=True, db_column='CO_TABLA_NUEVA', max_length=200, null=True)),
                ('co_tabla_temporal', models.CharField(blank=True, db_column='CO_TABLA_TEMPORAL', max_length=200, null=True)),
                ('nu_orden', models.FloatField(blank=True, db_column='NU_ORDEN', null=True)),
                ('co_lista', models.CharField(blank=True, db_column='CO_LISTA', max_length=100, null=True)),
                ('nu_orden_opcion', models.FloatField(blank=True, db_column='NU_ORDEN_OPCION', null=True)),
                ('nb_tabla_centipede', models.CharField(blank=True, db_column='NB_TABLA_CENTIPEDE', max_length=50, null=True)),
                ('co_visible', models.CharField(blank=True, db_column='CO_VISIBLE', max_length=50, null=True)),
                ('co_main', models.CharField(blank=True, db_column='CO_MAIN', max_length=50, null=True)),
                ('tx_tipo_opcion', models.CharField(blank=True, db_column='TX_TIPO_OPCION', max_length=50, null=True)),
                ('co_search', models.CharField(blank=True, db_column='CO_SEARCH', max_length=50, null=True)),
                ('tx_tipo_search', models.CharField(blank=True, db_column='TX_TIPO_SEARCH', max_length=50, null=True)),
                ('tx_procedure', models.CharField(blank=True, db_column='Tx_PROCEDURE', max_length=50, null=True)),
                ('tx_query', models.CharField(blank=True, db_column='Tx_QUERY', max_length=50, null=True)),
                ('tx_type_output', models.CharField(blank=True, db_column='TX_TYPE_OUTPUT', max_length=50, null=True)),
                ('co_output', models.CharField(blank=True, db_column='CO_OUTPUT', max_length=50, null=True)),
                ('tx_prefijo_export', models.CharField(blank=True, db_column='TX_PREFIJO_EXPORT', max_length=50, null=True)),
                ('nb_search', models.CharField(blank=True, db_column='NB_SEARCH', max_length=50, null=True)),
            ],
            options={
                'db_table': 'T_CENTIPANEL_MENU_NEW',
            },
        ),
    ]