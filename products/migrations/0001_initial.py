# Generated by Django 3.2.9 on 2022-06-02 12:07

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de Categoria')),
                ('nombreCategoria', models.CharField(max_length=200, verbose_name='Nombre Categoria')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria de Producto',
                'verbose_name_plural': 'Categorias de Productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del Producto')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre Producto')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('valor', models.FloatField(verbose_name='Valor del Producto')),
                ('alto', models.CharField(max_length=50, verbose_name='Medidas del Producto(Altura)')),
                ('largo', models.CharField(max_length=50, verbose_name='Medidas del Producto(Largo)')),
                ('ancho', models.CharField(max_length=50, verbose_name='Medidas del Producto(Anchura)')),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('calificacion', models.PositiveSmallIntegerField(default=0, verbose_name='Calificacion de productos')),
                ('imagen', models.TextField(blank=True, null=True, verbose_name='Nombre producto Imagenes')),
                ('imagen2', models.TextField(blank=True, null=True, verbose_name='Nombre producto Imagenes 2')),
                ('fechaInicio', models.DateField(verbose_name='Fecha de Inicio')),
                ('fechaFinalizacion', models.DateField(verbose_name='Fecha de Finalizacion')),
                ('estadoProducto', models.IntegerField(choices=[[0, 'Nuevo'], [1, 'Cancelado'], [2, 'Pendiente'], [3, 'Enviado'], [4, 'Produccion'], [5, 'Destacado']], default=0, verbose_name='Estado del Producto')),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoria', verbose_name='Indicador de Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('idPromociones', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de Promociones')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de la Promocion')),
                ('valorDescuento', models.PositiveSmallIntegerField(default=0, verbose_name='Valor del Descuento del Producto')),
                ('productoExtra', models.PositiveSmallIntegerField(default=0, verbose_name='Cantidad de Productos extra')),
                ('idProducto', models.ManyToManyField(to='products.Producto', verbose_name='Identificar del Producto')),
            ],
            options={
                'verbose_name': 'Promocion de Producto',
                'verbose_name_plural': 'Promociones de Productos',
            },
        ),
        migrations.CreateModel(
            name='HistoricalPromocion',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('idPromociones', models.IntegerField(blank=True, db_index=True, verbose_name='Identificador de Promociones')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de la Promocion')),
                ('valorDescuento', models.PositiveSmallIntegerField(default=0, verbose_name='Valor del Descuento del Producto')),
                ('productoExtra', models.PositiveSmallIntegerField(default=0, verbose_name='Cantidad de Productos extra')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.user')),
            ],
            options={
                'verbose_name': 'historical Promocion de Producto',
                'verbose_name_plural': 'historical Promociones de Productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProducto',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('idProducto', models.IntegerField(blank=True, db_index=True, verbose_name='Identificador del Producto')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre Producto')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('valor', models.FloatField(verbose_name='Valor del Producto')),
                ('alto', models.CharField(max_length=50, verbose_name='Medidas del Producto(Altura)')),
                ('largo', models.CharField(max_length=50, verbose_name='Medidas del Producto(Largo)')),
                ('ancho', models.CharField(max_length=50, verbose_name='Medidas del Producto(Anchura)')),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('calificacion', models.PositiveSmallIntegerField(default=0, verbose_name='Calificacion de productos')),
                ('imagen', models.TextField(blank=True, null=True, verbose_name='Nombre producto Imagenes')),
                ('imagen2', models.TextField(blank=True, null=True, verbose_name='Nombre producto Imagenes 2')),
                ('fechaInicio', models.DateField(verbose_name='Fecha de Inicio')),
                ('fechaFinalizacion', models.DateField(verbose_name='Fecha de Finalizacion')),
                ('estadoProducto', models.IntegerField(choices=[[0, 'Nuevo'], [1, 'Cancelado'], [2, 'Pendiente'], [3, 'Enviado'], [4, 'Produccion'], [5, 'Destacado']], default=0, verbose_name='Estado del Producto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.user')),
                ('idCategoria', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoria', verbose_name='Indicador de Categoria')),
            ],
            options={
                'verbose_name': 'historical Producto',
                'verbose_name_plural': 'historical Productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategoria',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('idCategoria', models.IntegerField(blank=True, db_index=True, verbose_name='Identificador de Categoria')),
                ('nombreCategoria', models.CharField(max_length=200, verbose_name='Nombre Categoria')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.user')),
            ],
            options={
                'verbose_name': 'historical Categoria de Producto',
                'verbose_name_plural': 'historical Categorias de Productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
