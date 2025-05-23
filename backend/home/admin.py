from django.contrib import admin
from home.models import ProductClass,ProductBelongsTo,Item
# Register your models here.
admin.site.register(ProductClass)
admin.site.register(ProductBelongsTo)
admin.site.register(Item)
