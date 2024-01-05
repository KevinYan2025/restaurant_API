from django.db import models
#User model is already being 
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    # slug store the URL-friendly version of the category's title.
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    class Meta:
        #creating an index on the title field can speed up lookups based on the title.
        indexes = [
            models.Index(fields=['title']),
        ]

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places = 2)
    featured = models.BooleanField()
    #models.PROTECH prevent Category object being detete when it is reference by one or more MenuItem object
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    class Meta:
        indexes = [
            models.Index(fields=['title','price','featured']),
        ]
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("user", "menuitem",), name="unique_menuitem"
            ),
        ]

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(
        #when user model is deletethe delivery_crew feild will be set to NULL
        User,on_delete=models.SET_NULL,
        related_name="delivery_crew",
        null = True
    )
    status = models.BooleanField(default=0)
    total = models.DecimalField(max_digits=6,decimal_places=2)
    date = models.DateField(default=timezone.now)
    class Meta:
        indexes = [
            models.Index(fields=['status','status']),
        ]

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("order", "menuitem",),
                name="unique_order"
            ),
        ]
