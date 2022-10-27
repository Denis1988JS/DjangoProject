from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User, Group

# Create your models here.

#Модель категории товаров
class CategoryOfGoods(models.Model):
    nameOfCategory= models.CharField(max_length=100,verbose_name='Категория товара')
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.nameOfCategory
    def get_absolute_url(self):
        return reverse('categoryGoods', kwargs={'slug':self.slug})
    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категория товаров'

#Модель производитель товара
class Manufacturer(models.Model):
    nameOfFactory = models.CharField(max_length=150, verbose_name='Компания производитель')
    def __str__(self):
        return self.nameOfFactory
    def get_absolute_url(self):
        return reverse('man', kwargs={'man_id':self.pk})
    class Meta:
        verbose_name = 'Производитель товара'
        verbose_name_plural = 'Производитель товара'

#Модель товары
class Goods(models.Model):
    nameOfGoods = models.CharField(max_length=150, verbose_name='Название товара')
    priceOfGoods = models.IntegerField(verbose_name='Цена')
    manufacturerOfGoods = models.ForeignKey(Manufacturer,null=True,on_delete=models.CASCADE, verbose_name='Производитель товара')
    dateAppGoods = models.DateField(auto_now_add=True,verbose_name='Дата добавления в каталог')
    imageGoods = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Каталог фото')
    categoryGoods = models.ForeignKey(CategoryOfGoods,null=True, on_delete=models.CASCADE, verbose_name='Категория товара')
    contexOfGoods = models.CharField(max_length=500,verbose_name='Описание товара')
    sellerGoods = models.ForeignKey(User,null=True, on_delete=models.CASCADE, verbose_name='Продавец товара')
    def __str__(self):
        return self.nameOfGoods
    def get_absolute_url(self):
        return reverse('goodsCatalog', kwargs={'pk':self.pk})
    class Meta:
        verbose_name_plural = 'Товары'

#Модель комментарии товаров
class CommentsOfGoods(models.Model):
    contextComment = models.CharField(max_length=250)
    idGoods = models.ForeignKey(Goods,null=True,blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null= True, blank=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Комментарии о товаре'

#Модель корзина покупок
class Basket(models.Model):
    zakazGuman = models.CharField(max_length=100)
    goodsZacaz = models.CharField(max_length=100, verbose_name='Название товара')
    countGoods = models.IntegerField(verbose_name='Кол-во товара')
    priceGoods = models.IntegerField(verbose_name='Цена за ед')
    sellerUser = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Продавец товара')
    def __str__(self):
        valSum = self.priceGoods * self.countGoods
        return f'{valSum}'











