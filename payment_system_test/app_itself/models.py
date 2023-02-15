from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price_id = models.CharField(max_length=100, null=True)
    product_id = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    currency = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name_plural = 'items'

    def get_item_by_id(id):
        try:
            item = Item.objects.get(id=id)

            return [item.name, item.price_id, item.product_id, item.description, item.price, item.currency] # Знаю, что передавать эти значения в виде списка
            # не очень правильно, но, поскольку в задаче нужно доставать лишь 1 item, мы 
            # всегда будем уверены в том, что находится в соответствующих индексах 
        except Exception as e:
            pass

    def __str__(self):
        return self.name