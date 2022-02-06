from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

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
    description = models.CharField(max_length=100, default="")

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
    product_user = models.ForeignKey("CustomUserModel",on_delete = models.DO_NOTHING, blank=False, null=True)

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

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        try:
            name = extra_fields.get('first_name')
            lname = extra_fields.get('last_name')
            if len(name):
                raise ValueError("first_name can not be empty")

            if len(lname):
                raise ValueError("last_name can not be empty")
        except:
            pass

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_manager', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin = True')

        return self.create_user(email, password, **extra_fields)

class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email adress', unique= True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default = timezone.now)
    first_name = models.CharField(max_length=15, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=9, blank=False, null=False)
    localization = models.ForeignKey(LocalizationModel, blank=False, null=True, on_delete= models.DO_NOTHING)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email}'

    def get_email(self):
        return self.email

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_is_staff(self):
        return self.is_staff

    def get_is_admin(self):
        return self.is_admin

    def get_is_manager(self):
        return self.is_manager

    def get_phone_number(self):
        return self.phone_number

    def get_localization(self):
        if self.localization:
            return self.localization
        
        return "That user have not set localization yet"

    def get_products(self):
        products = self.productmodel_set.all()
        return products

    def set_phone_number(self, number):
        if len(number) < 9:
            raise ValueError("Invalid number length, number to short")
        elif len(number) > 9:
            raise ValueError("Invalid number length, number to long")

        self.phone_number = number

        return self.phone_number

    def set_first_name(self, name):
        if len(name):
            self.first_name = name
        else:
            raise ValueError("Name can not be empty!!")

        return self.first_name

    def set_last_name(self, last_name):
        if len(last_name):
            self.last_name = last_name
        else:
            raise ValueError("Last name can not be empty")

        return self.last_name

    def set_is_admin(self, admin):
        self.is_admin = admin
        return self.is_admin

    def set_is_manager(self, manager):
        self.is_manager = manager
        return self.is_manager

    def set_email(self, email):
        try:
            CustomUserModel.objects.get(email= email)
        except:
            raise ValueError('User with that email is already exist')

        self.email = email

    def set_localization(self, localization):
        if isinstance(localization, LocalizationModel):
            self.localization = localization
        else:
            raise ValueError('')
        return self.localization
