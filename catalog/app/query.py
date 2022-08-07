from .models import Product, Catalog, Buyer

def get_products():
    buyer = Buyer.objects.first()
    buyer_products = buyer.products
    print('default_products', Product.objects.filter(visibility=Product.Visibility.DEFAULT))
    print('buyer_products', buyer_products)
    print('query', buyer_products.query)
    return buyer.products