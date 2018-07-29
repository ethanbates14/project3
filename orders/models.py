from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class Menu(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="category")
    menu_item = models.CharField(max_length=30)

    def __str__(self):
        return self.menu_item


class Prices(models.Model):
    ITEM_SIZES = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_size = models.CharField(max_length=1, choices=ITEM_SIZES)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item_size} {self.item_price}"