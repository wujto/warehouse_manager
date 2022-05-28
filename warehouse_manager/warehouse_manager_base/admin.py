from django.contrib import admin
from .models import LocalizationModel,CustomUserModel,CategoryModel,ProductModel

admin.site.register(LocalizationModel)
admin.site.register(CustomUserModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
