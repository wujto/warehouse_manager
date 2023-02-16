import os
from django.db import models

from users.models import Profile

def photo_upload_localization(instance, filename):
        return os.path.join('images/%s' % instance.id_number, filename)

class Product(models.Model):
    id_number = models.CharField(max_length=4, unique=True, blank=False)
    name = models.CharField(max_length=25, blank=False, null=False)
    description = models.TextField(max_length=50, blank=True, null=False)
    responsible_person = models.ForeignKey(Profile, blank=True, null=True, 
                                           default= None,
                                           related_name='products',
                                           on_delete=models.SET_DEFAULT)
    transfer_person = models.ForeignKey(Profile, blank=True, null=True,
                                        default=None, related_name='transfers',
                                        on_delete=models.SET_DEFAULT)
    photo = models.ImageField(upload_to=photo_upload_localization, 
                              blank=True, null=True,
                              default=None)
    add_date_time = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.id_number} | {self.name}'

    def delete(self):
        self.responsible_person = None
        self.transfer_person = None
        self.save()
        return super(Product,self).delete()

    def confirm_transfer(self):
        self.responsible_person = self.transfer_person
        self.transfer_person = None
        self.save()

    def reject_transfer(self):
        self.transfer_person = None
        self.save()
