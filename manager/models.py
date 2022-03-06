from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150,
                             verbose_name='Name of manager',
                             help_text='this is name of manager')
    data = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}  {self.id}"


class Comments(models.Model):
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')


class Marks(models.Model):
    mark = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Marks')


