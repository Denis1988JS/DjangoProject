# Generated by Django 4.0.4 on 2022-10-17 20:10

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
            name='CategoryOfGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfCategory', models.CharField(max_length=100, verbose_name='Категория товара')),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория товаров',
                'verbose_name_plural': 'Категория товаров',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfFactory', models.CharField(max_length=150, verbose_name='Компания производитель')),
            ],
            options={
                'verbose_name': 'Производитель товара',
                'verbose_name_plural': 'Производитель товара',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfGoods', models.CharField(max_length=150, verbose_name='Название товара')),
                ('priceOfGoods', models.IntegerField(verbose_name='Цена')),
                ('dateAppGoods', models.DateField(auto_now_add=True, verbose_name='Дата добавления в каталог')),
                ('imageGoods', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Каталог фото')),
                ('contexOfGoods', models.CharField(max_length=500, verbose_name='Описание товара')),
                ('categoryGoods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopPlatform.categoryofgoods', verbose_name='Категория товара')),
                ('manufacturerOfGoods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopPlatform.manufacturer', verbose_name='Производитель товара')),
                ('sellerGoods', models.ForeignKey(blank=True, null=True,on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Продавец товара')),
            ],
            options={
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='CommentsOfGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contextComment', models.CharField(max_length=250)),
                ('idGoods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopPlatform.goods')),
            ],
            options={
                'verbose_name_plural': 'Комментарии о товаре',
            },
        ),
    ]