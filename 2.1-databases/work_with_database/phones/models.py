from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    image = models.URLField()
    price = models.IntegerField()
    release_date = models.DateField()
    ite_exists = models.BooleanField()
    slug = models.SlugField()

