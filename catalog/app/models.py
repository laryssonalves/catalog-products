from django.db import models

# Create your models here.
class Product(models.Model):
    class Visibility(models.IntegerChoices):
        DEFAULT = 1
        CATALOG_MEMBERS = 2

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    visibility = models.IntegerField(choices=Visibility.choices, default=Visibility.DEFAULT)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Catalog(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name='catalogs')

    class Meta:
        db_table = 'catalog'
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'

    def __str__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(max_length=255)
    catalogs = models.ManyToManyField(Catalog, related_name='buyers')

    class Meta:
        db_table = 'buyer'
        verbose_name = 'Buyer'
        verbose_name_plural = 'Buyers'

    def __str__(self):
        return self.name

    @property
    def products(self):
        return Product.objects.filter(
            models.Q(catalogs__in=self.catalogs.all()) |
            models.Q(visibility=Product.Visibility.DEFAULT))