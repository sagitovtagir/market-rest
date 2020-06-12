from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Deal
from .serializers import DealSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer

# Представление страницы пользователя. Выводим данные на страницу
class UserDetail(APIView):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        data = UserSerializer(user).data
        return Response(data)

# Корзина пользователя. Выводятся товары, которые пользователь добавил в корзину. Сама корзина - это запись
# в таблице Deal с полем stage=0 (in_cart). Поле stage - это стадия сделки, то есть сначала в_корзине, потом Заказано,
# Оплачено и т. д. Тип этого поля - некая реализация enum. Сделал на будущее, когда дойдет до реализации этих
# бизнес-процессов.
class CartList(APIView):
    def get(self, request):
        cart = Deal.objects.filter(user_id=request.user.id, stage=0)
        data = DealSerializer(cart, many=True).data
        return Response(data)

# Представление для просмотра, изменения, удаления товара из корзины. На самом деле, такой страницы не будет
# на сайте, эти запросы будут выполняться с помощью скриптов. Добавление в корзину еще не сделал.
# Немного перегрузил функции класса для проверки, имеет ли право пользователь изменять и просматривать эти записи.

class DealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    def validate_user(self, message_error, request, *args, **kwargs, ):
        deal = Deal.objects.get(pk=self.kwargs['pk'])
        if not request.user == deal.user:
            raise PermissionDenied(message_error)

    def retrieve(self, request, *args, **kwargs):
        self.validate_user(request=request, message_error="Вы не можете просмотреть эту запись")
        return super().update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.validate_user(request=request, message_error="Вы не можете изменить эту запись")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.validate_user(request=request, message_error="Вы не можете удалить эту запись")
        return super().destroy(request, *args, **kwargs)

# Представление для создания пользователя
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

# Представление для входа на сайт. Получает логин и пароль. Возвращает токен пользователя.
# Токен далее надо добавить в хэдер запроса по типу Authorization: Token 1ee7e052525876e5288aa10febec2fa273a20f36

class LoginView(APIView):
    permission_classes = ()
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):
        return Response({})
    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)






