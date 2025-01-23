from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Model
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[ MinValueValidator(18),
                                                        MaxValueValidator(90)], null=True, blank=True)
    ROLE_CHOICES=(
        ('Клиент', 'Клиент'),
        ('Владелец', 'Владелец'),
        ('Администратор', 'Администратор'),
        ('Курьер', 'Курьер')
    )
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='Клиент')

    def __str__(self):
        return f'{self.first_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True )

    def __str__(self):
        return self.category_name



class Store(models.Model):
    store_name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    address = models.CharField(max_length=128)
    store_image = models.ImageField(upload_to='image/')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner_store')

    def __str__(self):
        return f'{self.store_name}'

    def get_avg_rating(self):
        ratings = self.store_review.all()
        if ratings.exists():
            return round(sum([i.rating for i in ratings]) / ratings.count(), 1)
        return 0


    def get_count_rating(self):
        ratings = self.store_review.all()
        if ratings.exists():
            if ratings.count() > 3:
                return '3+'
            return ratings.count()
        return 0




class Contact(models.Model):
    contact_info = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='contact')
    contact_number = PhoneNumberField(null=True, blank=True, region='KG')


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='image/')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_product')

    def __str__(self):
        return f'{self.product_name}'



class Combo(models.Model):
    combo_name = models.CharField(max_length=64)
    description = models.TextField()
    store = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='combo_for_store')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    combo_image = models.ImageField(upload_to='image/')

    def __str__(self):
        return f'{self.combo_name}, {self.price}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_cart', null=True, blank=True)
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)



class Order(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_order')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order')
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_order')
    delivery_address = models.CharField(max_length=128)
    STATUS_ORDER_CHOICES = (
        ('кутуп жатат', 'кутуп жатат'),
        ('алып бара жатат', 'алып бара жатат'),
        ('жеткирди', 'жеткирди'),
        ('отмена заказ', 'отмена заказ')
    )
    status_order = models.CharField(choices=STATUS_ORDER_CHOICES, max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)


class Courier(models.Model):   
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_user')
    STATUS_COURIER_CHOICES = (
        ('доступен', 'доступен'),
        ('занят', 'занят'),
    )
    status = models.CharField(choices=STATUS_COURIER_CHOICES, max_length=32)
    current_orders =models.ForeignKey(Order, on_delete=models.CASCADE, related_name='current_order')

    def __str__(self):
        return f'{self.user}'



class Review(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_review')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_review')
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_review')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                          MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return f'{self.client}'














