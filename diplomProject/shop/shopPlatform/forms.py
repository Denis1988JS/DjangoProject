from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import *
#Поиск товара
class SeachGoods(forms.Form):
    goodsName = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'formseach','placeholder':'Я ищу',}))

GEEKS_CHOICES = (
    (1,'Продавцы'),
    (2,'Покупатели'),
)
#Форма регистрации
class RegistForm(UserCreationForm):
    username = forms.CharField(label='Имя аккаунта',help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control' }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control' }))
    group = forms.ChoiceField(choices = GEEKS_CHOICES,label='Выберите группу пользователей',widget=forms.Select(attrs={'class': 'form-control', }))
    class Meta:
        model = User
        fields = ('username','password1','password2')

#Форма добавления товара от продавца
class NewGoods(forms.Form):
    nameOfGoods = forms.CharField(max_length=150, label='Название товара', required=True, )
    priceOfGoods = forms.IntegerField(label='Цена товара', required=True)
    manufacturerOfGoods = forms.ModelChoiceField(queryset=Manufacturer.objects.all(), label='Выберите производителя товара', required=False, )
    imageGoods = forms.ImageField(label='Добавьте фотографию товара', required=True)
    categoryGoods = forms.ModelChoiceField(queryset=CategoryOfGoods.objects.all(), label='Выберите категорию товара', required=False)
    contexOfGoods = forms.CharField(label='Введите описание товара', required=False, widget=forms.Textarea(attrs={'cols': 100,
                                                                                                                         'rows': 10}))
#Изменение существующего товара
class CreateGoods(forms.Form):
    nameOfGoods = forms.CharField(max_length=150, label='Название товара',)
    priceOfGoods = forms.IntegerField(label='Цена товара', required=True,)
    manufacturerOfGoods = forms.ModelChoiceField(queryset=Manufacturer.objects.all(),label='Выберите производителя товара', required=False,)
    imageGoods = forms.FileField(label='Добавьте фотографию товара', required=True)
    categoryGoods = forms.ModelChoiceField(queryset=CategoryOfGoods.objects.all(),label='Выберите категорию товара', required=False)
    contexOfGoods = forms.CharField(label='Выберите категорию товара', required=False, widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))

#Создание коментария пользователем о товаре
class CreateComments(forms.ModelForm):
    class Meta:
        model = CommentsOfGoods
        fields = ['contextComment']
        widgets = {
            'contextComment': forms.Textarea(attrs={'rows':10,'class': 'form-control'})
        }

#Форма для заказа
class BasketForm(forms.Form):
        countGoods =forms.IntegerField(label='Введите кол-во товара')





























