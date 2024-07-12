# Generated by Django 3.0.6 on 2024-07-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('cat_image', models.ImageField(blank=True, upload_to='photos/categories')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
