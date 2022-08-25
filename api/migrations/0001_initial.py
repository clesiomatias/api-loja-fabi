# Generated by Django 4.1 on 2022-08-24 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('qtd_em_estoque', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cor', models.CharField(max_length=50)),
                ('tamanho', models.PositiveIntegerField()),
                ('imagem', models.ImageField(upload_to='')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sub_Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('A', 'Adulto'), ('I', 'Infantil'), ('P', 'Plus_Size')], max_length=1)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('cam', 'Camisetas'), ('blu', 'Blusas'), ('sho', 'Shorts'), ('cal', 'Calça'), ('int', 'Roupa_Intima')], max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Tipos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Carrinho'), (2, 'Realizado'), (3, 'Pago'), (4, 'Entregue')], default=1)),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='venda', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendaItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.venda')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='s_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sub_categoria'),
        ),
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipos'),
        ),
    ]
