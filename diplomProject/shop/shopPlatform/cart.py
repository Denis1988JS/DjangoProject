from decimal import Decimal
import requests
from shop import settings
from .models import Goods, Group

class Cart(object):
    def __init__(self):
        self.session = requests.Session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]= {}
        self.cart = cart

    #Перебор товаров в корзине и получаем товары из базы данных
    def __iter__(self):
        goods_ids = self.cart.keys()
        goods = Goods.objects.filter(id__in=goods_ids)
        cart = self.cart.copy()
        for g in goods:
            cart[str(goods.id)]['goods'] = g
        for i in cart.values():
            i['price'] = Decimal(i['price'])
            i['total_price'] = i['price'] * i['quantity']
            yield i

    #Кол-во товаров в корзине
    def __len__(self):
        return sum(i['quantity'] for i in self.cart.values())

    #Добавляем в корзину
    def add(self, goods, quantity = 1 , update_quantity = False):
        goods_id = str(goods.id)
        if goods_id not in self.cart:
            self.cart[goods_id] = {'quantity':0, 'price': str(goods.priceOfGoods)}
        if update_quantity:
            self.cart[goods_id]['quantity'] = quantity
        else:
            self.cart[goods_id]['quantity'] += quantity
        self.save()

    #Сохранение корзины
    def save(self):
        self.session.modified = True

    #Удаление из корзины товара
    def remove(self, goods):
        goods_id = str(goods.id)
        if goods_id in self.cart:
            del self.cart[goods_id]
            self.save()
    def get_total_price(self):
        return
