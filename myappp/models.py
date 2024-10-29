from django.db import models
# Create your models here.

class register(models.Model):
    
    name = models.CharField(max_length=200)

    email = models.CharField(max_length=200)

    password = models.CharField(max_length=200)


class news_data(models.Model):

    img_path = models.CharField(max_length=200)

    category_name = models.CharField(max_length=200)

    name = models.CharField(max_length=200)

    description = models.CharField(max_length=200)
    

class xeber_yukle(models.Model):

    img_path_yukle = models.CharField(max_length=200)

    category_name_yukle = models.CharField(max_length=200)

    name_yukle = models.CharField(max_length=200)

    description_yukle = models.CharField(max_length=200)
    