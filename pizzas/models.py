from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=30)
    #date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pizza_name # + '-' + str(self.date_added)

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    topping_name = models.TextField()
    #date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topping_name[:30]}"


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    comment_name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_name[:50]}"


