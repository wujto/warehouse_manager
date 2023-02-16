import os
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def phone_number_validation(value):
    if len(value) != 9:
        raise ValidationError('Phone number must have 9 numbers!')

    if not value.isnumeric():
        raise ValidationError('Phone number must have only numbers')
    
    return value

def photo_upload_localization(instance, filename):
        return os.path.join(f'images/{instance.user.username}_{instance.user.lastname}',
                             filename)

class Localization(models.Model):
    name = models.CharField(max_length=20, blank=False)

    class Meta:
        verbose_name = 'Localization'
        verbose_name_plural = 'Localizations'

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False,
                                null=False, related_name='profile')
    phone_number = models.CharField(validators=[phone_number_validation], 
                                    blank=True, default='', max_length=9)
    localization = models.ForeignKey(Localization, 
                                     on_delete=models.SET_DEFAULT, default=1)
    photo = models.ImageField(upload_to=photo_upload_localization, blank=True, null=True,
                              default=None)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    
    def __str__(self):
        return f'{self.user.username} {self.user.last_name}'

    def delete(self):
        self.user = None
        self.localization = None
        self.photo = None
        self.save()
        return super(Profile, self).delete()

    def save(self, *args, **kwargs):
        phone_number_validation(self.phone_number)
        return super(Profile, self).save(*args, **kwargs)
