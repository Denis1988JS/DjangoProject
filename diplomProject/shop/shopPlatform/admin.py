from django.contrib import admin
from django.utils.safestring import mark_safe

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
    list_display = ('nameOfGoods','priceOfGoods','manufacturerOfGoods','dateAppGoods','categoryGoods','contexOfGoods','getImage')
    list_filter = ('categoryGoods','sellerGoods')
    search_fields = ('nameOfGoods','categoryGoods__nameOfCategory')
    def getImage(self, obj):
        return mark_safe(f'<img src={obj.imageGoods.url} width="50" height="50">')
    getImage.short_description = 'Фото'
@admin.register(CommentsOfGoods)
class CommentsOfGoods(admin.ModelAdmin):
    list_display = ('idGoods', 'contextComment')
    list_filter = ('idGoods',)
