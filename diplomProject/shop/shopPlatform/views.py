import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.core.mail import message
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import *
from .models import *
from django.http import *
# Create your views here.
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistForm, NewGoods
from django.contrib.auth import get_user_model
from django.conf import settings

listCategory = []
#Представление главной страницы
def index(request):
    title = 'SellAndBuy'
    if request.method == "POST":
        formSeach =  SeachGoods()
        if formSeach.is_valid():
            return HttpResponseRedirect('')
    else:
        formSeach = SeachGoods()
        listCategory = CategoryOfGoods.objects.all()
        good = Goods.objects.all()
        data = {'listCategory': listCategory,'formSeach':formSeach, 'title':title}

    return render(request, 'shopTemplates/index.html', context=data)

#Представление все товары
class GoodsListView(ListView):
    paginate_by = 10
    model = Goods
    template_name = 'shopTemplates/goodsCatalog.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listCategory'] = CategoryOfGoods.objects.all()
        context['title'] = 'Каталог товаров'
        return context

#Представление по товарно
class ShowGoods(DetailView):
    model = Goods
    template_name = 'shopTemplates/goodDetail.html'
    context_object_name = 'good'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listCategory'] = CategoryOfGoods.objects.all()
        context['comments'] = CommentsOfGoods.objects.filter(idGoods=self.kwargs['pk'])
        context['userGroup'] = self.request.user.groups.all()
        context['form'] = BasketForm()
        return context

#Корзина заполнения
def mybasket(request, id):
    if request.method == "POST":
        form =  BasketForm()
        basket = Basket()
        goods = Goods.objects.get(id=id)
        basket.zakazGuman = User.objects.get(id=request.user.id)
        basket.goodsZacaz = goods.nameOfGoods
        basket.countGoods = request.POST.get('countGoods')
        basket.priceGoods = goods.priceOfGoods
        basket.sellerUser = goods.sellerGoods
        basket.save()
    return  redirect('/goodsCatalog')

#Корзина корректировки и подтверждение заказа
class FinalBasket(ListView):
    model = Basket
    template_name = 'shopTemplates/finalBasket.html'
    context_object_name = 'basket'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userName = self.request.user
        context['listCategory'] = CategoryOfGoods.objects.all()
        context['basket'] = Basket.objects.filter(zakazGuman=userName)
        context['title'] = 'Корзина покупок'
        return context

#Удаление товар из корзины
def delBG(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return redirect('/finalbasket')

#Просмотр заказов от покупателей

class ShowZakaz(ListView):
    model = Basket
    template_name = 'shopTemplates/showZacaz.html'
    context_object_name = 'zakaz'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sellerName = self.request.user
        context['listCategory'] = CategoryOfGoods.objects.all()
        context['basket'] = Basket.objects.filter(sellerUser=sellerName)
        return context

#Представление по категориям
class ShowGoodsCategory(ListView):
    paginate_by = 20
    model = Goods
    template_name = 'shopTemplates/goodsCategory.html'
    context_object_name = 'goods'
    def get_queryset(self):
        return Goods.objects.filter(categoryGoods__slug=self.kwargs['slug'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listCategory'] = CategoryOfGoods.objects.all()
        context['category'] = CategoryOfGoods.objects.get(slug=self.kwargs['slug'])
        return context

#Представление результат поиска
class RezultSeach(ListView):
    paginate_by = 20
    model = Goods
    template_name = 'shopTemplates/rezultSeach.html'
    context_object_name = 'goods'
    def get_queryset(self):
        queryForm = self.request.GET.get('goodsName')
        object_list = Goods.objects.filter(nameOfGoods__icontains=queryForm)
        return object_list

#Представление страница о сайте
class AboutList(ListView):
    model = Goods
    template_name = 'shopTemplates/about.html'
    context_object_name = 'goods'
    User = get_user_model()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listCategory'] = CategoryOfGoods.objects.all()
        context['catCount'] = CategoryOfGoods.objects.all().count
        context['goodsCount'] = Goods.objects.all().count
        context['users'] = User.objects.all()
        context['title'] = 'О нас'
        context['userGroup'] = User.objects.filter(groups__id=1).count()
        return context

#Регистрация пользователя
def register(request):
    data = {'title':'Регистрация'}
    if request.method == 'POST':
        form = RegistForm(request.POST)
        user = form.save()
        group = Group.objects.get(id=request.POST.get('group'))
        group.user_set.add(user)
        return render(request,'shopTemplates/index.html', context=data)

    else:
        form = RegistForm()
        data['form']=form
        return render(request, 'shopTemplates/register.html', data)

#Управление данными пользователя
class UserCabinet(ListView):
    model = Goods
    template_name = 'shopTemplates/sellerDetail.html'
    context_object_name = 'goods'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userName_1 = self.request.user.id
        object_list = Goods.objects.filter(sellerGoods=userName_1)
        context['NewGoods'] = NewGoods()
        context['object_list'] = object_list
        context['title'] = 'Личный кабинет'
        context['userGroup'] = self.request.user.groups.all()
        return context

#Добавление нового товара от продавца
def addGood(request):
    goods = Goods()
    if request.method == 'POST':
        form = NewGoods(request.POST, request.FILES)
        if form.is_valid():
            goods.nameOfGoods = request.POST.get('nameOfGoods')
            goods.priceOfGoods = request.POST.get('priceOfGoods')
            goods.manufacturerOfGoods = Manufacturer.objects.get(id=request.POST.get('manufacturerOfGoods'))
            goods.imageGoods = request.FILES['imageGoods']
            goods.categoryGoods =CategoryOfGoods.objects.get(id=request.POST.get('categoryGoods'))
            goods.contexOfGoods = request.POST.get('contexOfGoods')
            goods.sellerGoods = User.objects.get(id=request.user.id)
            print(form.cleaned_data)
            goods.save()
            return redirect('cabinet')
    else:
        form = NewGoods(request.POST, request.FILES)
    data = {'form': form}
    return render(request, 'shopTemplates/addGood.html', {'form': form})

#Изменение товара у продавца
def editGoods(request, id):
    goods = Goods.objects.get(id=id)
    if request.method == 'POST':
        form = CreateGoods(request.POST, request.FILES)
        if form.is_valid():
            goods.nameOfGoods = request.POST.get('nameOfGoods')
            goods.priceOfGoods = request.POST.get('priceOfGoods')
            goods.Manufacturer = request.POST.get('manufacturerOfGoods')
            goods.imageGoods = request.FILES['imageGoods']
            goods.CategoryOfGoods = request.POST.get('categoryGoods')
            goods.contexOfGoods = request.POST.get('contexOfGoods')
            goods.User = request.user
            goods.save()
            return redirect('cabinet')
        else:
            return redirect("addGood")
    else:
        form = CreateGoods(request.POST, request.FILES)
    data = {'goods': goods, 'form': form}
    return render(request, 'shopTemplates/editGoods.html', context=data)

#Удаление товара у продавца
def delGoods(request, id):
    goods = Goods.objects.get(id=id)
    goods.delete()
    return redirect('cabinet')

#Добавление комментария
def commentGoods(request, id):
    goods = Goods.objects.get(id=id)
    title = 'Комментарий к товару'
    if request.method == 'POST':
        form = CreateComments(request.POST)
        if form.is_valid():
            comment = CommentsOfGoods()
            comment.idGoods = Goods.objects.get(id=id)
            comment.user = User.objects.get(id=request.user.id)
            comment.contextComment = request.POST.get('contextComment')
            comment.save()
            return redirect('listCatalog')
    else:
        form = CreateComments()
    data = {'good': goods, 'form': form, 'title':title}
    return render(request, 'shopTemplates/createComments.html', context=data)











