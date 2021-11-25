# Generated by Django 3.2.9 on 2021-11-08 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'marca',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarjetas', models.CharField(choices=[('marcado pago', 'mercado pago'), ('aula', 'aula'), ('efectivo', 'efectivo')], max_length=12)),
            ],
            options={
                'db_table': 'pago',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(default=0)),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.pago')),
            ],
            options={
                'db_table': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.FloatField(default=0)),
                ('imagen', models.ImageField(upload_to='img')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.marca')),
            ],
            options={
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='TipoEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoenvio', models.CharField(choices=[('envio domicilio', 'envio domicilio'), ('retiro al local', 'retiro al local')], max_length=15)),
            ],
            options={
                'db_table': 'tipo_envio',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contaseña', models.CharField(max_length=100)),
                ('email', models.EmailField(default=0, max_length=254)),
                ('celular', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='UsuarioPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('padido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.pedido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.usuarios')),
            ],
            options={
                'db_table': 'usuario_pedido',
            },
        ),
        migrations.CreateModel(
            name='ProductoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.producto')),
            ],
            options={
                'db_table': 'producto_pedido',
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipoenvio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.tipoenvio'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptarea.usuarios'),
        ),
    ]
