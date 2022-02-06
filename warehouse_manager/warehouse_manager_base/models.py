from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

class ProductSetModel(models.Model):
    id_number = models.CharField(max_length=9, unique=True, blank=False, null=False)
    name = models.CharField(max_length=25, blank=False, null=False)
    description = models.CharField(max_length=100, default="")
    products_count = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.id_number} {self.name}'

    def get_info(self):
        info ={'id_number': self.id_number,
        "name": self.name,
        "description":self.description,
        'products_count': self.products_count,
        }

        return info

    def edit_name(self, name):
        try:
            self.name = name
        except:
            return False
        return True

    def edit_description(self, description):
        self.description = description

class LocalizationModel(models.Model):
    name = models.CharField(unique=True, max_length=25, blank=False, null=False)
    description = models.CharField(max_length=50, default= "")

    def __str__(self):
        return self.name
    
    def get_description(self):
        return self.description

    def edit_name(self, name):
        # if len(name) == 0:
        #     raise Exception("Localization name must be longer!!")

        try:
            self.name = name
        except:
            return False
        return True

    def edit_description(self, description):
        self.description = description

class CategoryModel(models.Model):
    name = models.CharField(unique=True, max_length=15, blank=False, null=False)
    description = models.CharField(max_length=100, defalut="")

    def __str__(self):
        return self.name

    def get_description(self):
        return self.description
    
    def edit_description(self, description):
        self.description = description

    def edit_name(self, name):
        try:
            self.name = name
        except:
            return False
        return True

class ProductModel(models.Model):
    id_number = models.CharField(unique=True, max_length=9) #Number to identify product in database
    name = models.CharField(max_length=25, blank=False, null=False)
    description = models.CharField(max_length=100, default="")
    category = models.ForeignKey(CategoryModel, on_delete= models.DO_NOTHING, blank=False, null=False)
    localization = models.ForeignKey(LocalizationModel, on_delete = models.DO_NOTHING, blank=False, null=False)
    photo = models.FileField()
    product_set = models.ForeignKey(ProductSetModel,on_delete = models.DO_NOTHING, null=True, blank=False)
    product_user = models.ForeignKey("User",on_delete = models.DO_NOTHING, blank=False, null=True)

    def __str__(self):
        return f'{self.id_number} {self.name}'

    def get_info(self):
        info = {
            'id_number':self.id_number,
            'name':self.name,
            'description':self.description,
            'category':self.category,
            'localization':self.localization,
            'photo':self.photo,
            'product_set':self.product_set,
            'product_user':self.product_user
        }

        return info

# Edit name, description, category, localization
    def edit_info(self, info):
        self.name = info['name']
        self.description = info['description']
        self.category = info['category']
        self.localization = info['localization']

    def set_photo(self, photo):
        self.photo = photo

    def set_product_set(self, product_set):
        self.product_set = product_set

    def set_product_user(self, user):
        self.product_user = user


class CustomeUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)