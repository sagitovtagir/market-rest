"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mysite import views
from mysite import apiviews

# Роутинг не использовал в этом проекте, так как мне он не пригодился. Но в принципе понятно, как он работает.
#Рут - user, пароль - 123456.
# Представления Django rest находятся в файле apiviews.
# Пока что можно просмотреть емэйл и логин текущего авторизованного пользователя,
# просмотреть его корзину, удалить из корзины товары, изменить количество товара в корзине.
# Делать это пока приходится с помощью http-запросов.
# Чтобы залогиниться, надо в пути localhost:8000/login/ методом POST передать логин и пароль:
# {"username:client", "password": "mypassword"}. Вернется токен, который можно вставлять в заголовки
# запросов по типу Authorization: Token 1235252jjge342 (я использовал Postman для создания запросов).
# Чтобы просмотреть товары в корзине текущего авторизованного пользователя, надо отправить GET-запрос
# на адрес localhost:8000/user/cart/
# Чтобы изменить количество товара в корзине, надо залогиниться и указать в пути id товара в корзине
# (запись в таблице Deal):
# localhost:8000/user/cart/10
# и отправить по этому пути PUT-Запрос:
# {"user_count_product":"50"}
# Чтобы удалить товар из корзины, надо аналогично в пути указать id сделки и отправить запрос DELETE.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('category/', views.category),
    path('product/', views.product),
    path('login/', apiviews.LoginView.as_view(), name='login'),
    path('user/create/', apiviews.UserCreate.as_view(), name='user_create'),
    path('user/', apiviews.UserDetail.as_view(), name='users_detail'),
    path('user/cart/', apiviews.CartList.as_view(), name='cart_list'),
    path('user/cart/<int:pk>', apiviews.DealDetail.as_view(), name='deal_detail'),

]

# В проде убрать!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)