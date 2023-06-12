from django.db import models


# Create your models here.
from django.urls import reverse


class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=40)
    image = models.ImageField(upload_to="images/", blank=True)
    slug = models.SlugField(null=True)
    actif = models.BooleanField(default=True)
 
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("update", kwargs={"my_id": self.pk})


"""
python3 manage.py makemigrations
python3 manage.py migrate

"""
