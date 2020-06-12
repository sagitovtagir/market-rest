
from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(verbose_name='Название',
                            max_length=255,
                            unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(verbose_name='Описание',
                                   max_length=4095,
                                   blank=True)
    is_active = models.BooleanField(default=True,
                                    verbose_name='Активная')
    image = models.ImageField(verbose_name='Изображение',
                              null=False,
                              default='',
                              blank=True,
                              upload_to='images/category')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    category = TreeForeignKey(Category,
                              on_delete=models.SET_DEFAULT,
                              default=16,
                              null=False,
                              blank=False,
                              verbose_name='Категория'
                              )
    name = models.CharField(verbose_name='Название',
                            max_length=255,
                            default='')
    articul = models.CharField(verbose_name='Артикул',
                               max_length=255,
                               null=True,
                               blank=False,
                               unique=True)
    price = models.FloatField(verbose_name='Цена',
                              default=0,
                              blank=True,
                              null=False)
    description = models.TextField(verbose_name='Описание',
                                   max_length=4095,
                                   default='',
                                   blank=True)
    is_active = models.BooleanField(default=True,
                                    verbose_name='Есть на складе')
    preview = models.ImageField(verbose_name='Превью',
                                null=True,
                                blank=True,
                                upload_to='images/product_preview')
    count_product = models.IntegerField(verbose_name='Количество',
                                        null=False,
                                        default=0,
                                        blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(verbose_name='Изображение',
                              null=False,
                              default='',
                              blank=True,
                              upload_to='images/product')


    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'

class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name = 'Заказы'

class Deal(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    order = models.ForeignKey(Order,
                              on_delete=models.PROTECT,
                              verbose_name='Заказ', null=True, blank=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Товар')
    user_count_product = models.IntegerField(verbose_name='Количество',
                                      null=False,
                                      blank=True,
                                      default=1)
    STAGECHOICE = (('0', 'in_cart'), ('1', 'ordered'), ('2', 'paid'), ('3', 'delivered'), ('4', 'received'))
    stage = models.CharField(max_length=1, choices=STAGECHOICE)

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
