# Generated by Django 3.2.3 on 2021-07-02 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
        ('Clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('date_sale', models.DateTimeField(auto_now_add=True, verbose_name='fecha de venta')),
                ('total_price', models.IntegerField(verbose_name='precio total')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.client', verbose_name='comprador')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='vendedor')),
            ],
            options={
                'verbose_name': 'venta',
                'verbose_name_plural': 'ventas',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSale',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('date_sale', models.DateTimeField(blank=True, editable=False, verbose_name='fecha de venta')),
                ('total_price', models.IntegerField(verbose_name='precio total')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Clients.client', verbose_name='comprador')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='vendedor')),
            ],
            options={
                'verbose_name': 'historical venta',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDetailSale',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('cantidad', models.IntegerField(null=True, verbose_name='Cantidad por detalle')),
                ('precio', models.IntegerField(null=True, verbose_name='Precio del detalle')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Products.product')),
                ('sale', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Sales.sale', verbose_name='boleta de de venta')),
            ],
            options={
                'verbose_name': 'historical detalle de ventas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='DetailSale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('cantidad', models.IntegerField(null=True, verbose_name='Cantidad por detalle')),
                ('precio', models.IntegerField(null=True, verbose_name='Precio del detalle')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.sale', verbose_name='boleta de de venta')),
            ],
            options={
                'verbose_name': 'detalle de ventas',
                'verbose_name_plural': 'detalles de ventas',
            },
        ),
    ]
