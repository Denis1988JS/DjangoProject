from django.contrib import admin
from .models import CategoryOfGoods, Manufacturer, Goods, CommentsOfGoods

# Register your models here.
@admin.register(CategoryOfGoods)
class CategoryOfGoodsAdmin(admin.ModelAdmin):
    list_display = ('nameOfCategory','slug',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('nameOfFactory',)

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('nameOfGoods','priceOfGoods','manufacturerOfGoods','dateAppGoods','categoryGoods','contexOfGoods','imageGoods')
    list_filter = ('categoryGoods','priceOfGoods')

@admin.register(CommentsOfGoods)
class CommentsOfGoods(admin.ModelAdmin):
    list_display = ('idGoods', 'contextComment')
    list_filter = ('idGoods',)
