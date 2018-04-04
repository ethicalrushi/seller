from django.contrib import admin
from basic_app.models import Department , Product, Cart, ProductOrder

# Register your models here.
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Cart)
admin.site.register(ProductOrder)