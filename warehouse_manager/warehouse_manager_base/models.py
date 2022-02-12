from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class ProductSetModel(models.Model):
    id_number = models.CharField(max_length=9, unique=True, blank=False, null=False)
    name = models.CharField(max_length=25, blank=False, null=False)
    description = models.CharField(max_length=100, default="")
    products_count = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['name']
        permissions = [('is_manager','Can create, edit and delete')]
        verbose_name = 'products set'
        verbose_name_plural = 'products sets'

    def __str__(self):
        return f'{self.id_number} {self.name}'

    def get_info(self):
        info ={'id_number': self.id_number,
        "name": self.name,
        "description":self.description,
        'products_count': self.products_count,
        }

        return info

class LocalizationModel(models.Model):
    name = models.CharField(unique=True, max_length=25, blank=False, null=False)
    description = models.CharField(max_length=50, default= "")

    class Meta:
        ordering = ['name']
        permissions = [('is_manager','Can create, edit and delete')]
        verbose_name = 'localization'
        verbose_name_plural = 'localizations'

    def __str__(self):
        return self.name

class CategoryModel(models.Model):
    name = models.CharField(unique=True, max_length=15, blank=False, null=False)
    description = models.CharField(max_length=100, default="")

    class Meta:
        ordering = ['name']
        permissions = [('is_manager','Can create, edit and delete')]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    id_number = models.CharField(unique=True, max_length=9) #Number to identify product in database
    name = models.CharField(max_length=25, blank=False, null=False)
    description = models.CharField(max_length=100, default="")
    category = models.ForeignKey(CategoryModel, on_delete= models.DO_NOTHING, blank=False, null=False, related_name='products')
    localization = models.ForeignKey(LocalizationModel, on_delete = models.DO_NOTHING, blank=False, null=False, related_name='products')
    photo = models.FileField(upload_to="products/",null= True, blank= False)
    product_set = models.ForeignKey(ProductSetModel,on_delete = models.DO_NOTHING, null=True, blank=False, related_name='products')
    product_user = models.ForeignKey("CustomUserModel",on_delete = models.DO_NOTHING, blank=False, null=True, related_name='products')

    class Meta:
        ordering = ['name']
        permissions = [('is_manager','Can create, edit and delete')]
        verbose_name = 'product'
        verbose_name_plural = 'products'

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
    localization = models.ForeignKey(LocalizationModel, blank=False, null=True, on_delete= models.DO_NOTHING, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['first_name']
        permissions = [('is_admin','Can create and delete')]
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email}'

class ConfirmationOfTransfer(models.Model):
    CHOICES = (('PENDING','Pending'),# Waiting for confirm or reject
    ('CONFIRMED','Confirmed'),#Product can be assigned to new owner and confirmation can be destroyed
    ('REJECTED','Rejected'))#Product can`t be assigned to new owner and confirmation can be destroyed

    product = models.ForeignKey(ProductModel,on_delete= models.DO_NOTHING, related_name='confirmations')
    owner = models.ForeignKey(CustomUserModel, on_delete= models.DO_NOTHING, related_name='owned_confirmations')
    recipient = models.ForeignKey(CustomUserModel, on_delete= models.DO_NOTHING, related_name='recipient_confirmations')
    status = models.CharField(max_length=15, choices=CHOICES)
    date = models.DateTimeField(default= timezone.now)

    class Meta:
        ordering = ['-date']
        permissions = [('is_owner','Can create and delete'),
        ('is_recipient','Can edit status and delete')]
        verbose_name = 'confirmation'
        verbose_name_plural = 'confirmations'