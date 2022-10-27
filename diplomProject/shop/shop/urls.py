"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shopPlatform import views
from shopPlatform.views import GoodsListView, ShowGoods, ShowGoodsCategory, RezultSeach, AboutList, UserCabinet, editGoods,delGoods, \
    FinalBasket, delBG, ShowZakaz

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',AboutList.as_view(),name='about' ),
    path('goodsCatalog/',GoodsListView.as_view(),name='listCatalog'),
    path('goodsCatalog/<int:pk>/', ShowGoods.as_view(), name='goodsCatalog'),
    path('category/<slug:slug>/',ShowGoodsCategory.as_view(), name='categoryGoods'),
    path('rezultSeach/',RezultSeach.as_view(), name='rezultSeach'),
    path('admin/', admin.site.urls),
    path('register/',views.register, name='register'),
    path('cabinet/',UserCabinet.as_view(), name='cabinet'),
    path('addGood/',views.addGood, name='addGood'),
    path('cabinet/editGoods/<int:id>/', views.editGoods,name='editGoods' ),
    path('cabinet/delete/<int:id>/', views.delGoods,name='delete' ),
    path('createComments/<int:id>', views.commentGoods, name='createComments'),
    #Корзина
    path('finalbasket/',FinalBasket.as_view(), name = 'finalBasket'),
    path('finalbasket/delete/<int:id>/', views.delBG,name='delBG' ),
    path('mybasket/<int:id>', views.mybasket, name='mybasket'),
    path('showZacaz/', ShowZakaz.as_view(), name='showZakaz'),
    ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    ]