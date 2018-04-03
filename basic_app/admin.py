from django.contrib import admin
from basic_app.models import Department , Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Department)