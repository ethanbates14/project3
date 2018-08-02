from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class Options(models.Model):
    option_name = models.CharField(max_length=30)

    def __str__(self):
        return self.option_name

class Menu(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="category")
    menu_item = models.CharField(max_length=30)
    menu_options = models.ForeignKey(Options,models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.menu_item

class Topping(models.Model):
    topping_name = models.CharField(max_length=30)
    option_type = models.ForeignKey(Options,models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.topping_name

class Prices(models.Model):
    ITEM_SIZES = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_size = models.CharField(max_length=1, choices=ITEM_SIZES)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.menu_id} {self.item_size} {self.item_price}"

class Orders(models.Model):
    ORDER_STATUS = (
        ('P', 'Pending'),
        ('C', 'Completed'),
    )
    user_id = models.IntegerField()
    item_number = models.ForeignKey(Prices, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_details = models.CharField(max_length=250,blank=True)
    order_date = models.DateField()
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS,default="P")
