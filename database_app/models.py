from django.db import models

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=25)
    # Actually in real time projects Customer name and other related information should stored in different table.
    # And in Order table we just need to attach Customer with order using it's foreign key as follows.
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    total_items = models.IntegerField()
    price = models.IntegerField()
    is_delivered = models.BooleanField()

    def __str__(self):
        return self.customer_name