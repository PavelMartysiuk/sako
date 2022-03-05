from django.db import models

from core.models.utils import ModelMethods

from core.validators.model_validators import SizeValidators

import os

from django.contrib.postgres.fields import ArrayField


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(
        null=True,
        upload_to=ModelMethods.get_upload_path,
        blank=True,
        validators=[SizeValidators.image_size_validator],
    )

    def image_path(self):
        return os.path.join(f'manufacturer_logo/{self.id}')

    def __str__(self):
        return self.name


# Search о частичному
# Category + product + пагинация
# Фильтр массик категорий + новинка + производитель у товара, пагинация
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    #   image M2M
    name = models.CharField(max_length=50)
    descrtiption = models.CharField(max_length=400)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    manufactor = models.ForeignKey('Manufacturer', related_name='products', on_delete=models.CASCADE)
    availability = models.BooleanField()
    new = models.BooleanField()
    main_logo = models.ImageField(
        upload_to=ModelMethods.get_upload_path,
        validators=[SizeValidators.image_size_validator],
    )
    bestseller = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def image_path(self):
        return os.path.join(f'product_main_logo/{self.id}')


class ProductLogo(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_logo')
    logo = models.ImageField(
        upload_to=ModelMethods.get_upload_path,
    )

    def image_path(self):
        return os.path.join(f'product_logo/{self.id}')

    def __str__(self):
        return f'{self.product.name} {self.logo.name}'


class Partner(models.Model):
    name = models.CharField(max_length=40)
    logo = models.ImageField(
        null=True,
        upload_to=ModelMethods.get_upload_path,
        blank=True,
        validators=[SizeValidators.image_size_validator],
    )
    url = models.URLField()

    def __str__(self):
        return self.name

    def image_path(self):
        return os.path.join(f'partner_logo/{self.id}')


class About(models.Model):
    text = models.CharField(max_length=50000)

    def __str__(self):
        return self.text


class Contacts(models.Model):
    address = models.CharField(max_length=300)
    phones = ArrayField(models.CharField(max_length=100))
    email = models.EmailField()

    def __str__(self):
        return self.email
