# Generated by Django 3.2.9 on 2022-06-12 20:53

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo electronico')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombres')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellidos')),
                ('image', models.TextField(blank=True, default='', null=True, verbose_name='Imagen de perfil')),
                ('rolUser', models.CharField(default='Cliente', max_length=30, verbose_name='Rol de usuarios')),
                ('direccion', models.TextField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='activo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255)),
                ('email', models.EmailField(db_index=True, max_length=255, verbose_name='Correo electronico')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombres')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellidos')),
                ('image', models.TextField(blank=True, default='', null=True, verbose_name='Imagen de perfil')),
                ('rolUser', models.CharField(default='Cliente', max_length=30, verbose_name='Rol de usuarios')),
                ('direccion', models.TextField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='activo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.user')),
            ],
            options={
                'verbose_name': 'historical Usuario',
                'verbose_name_plural': 'historical Usuarios',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
