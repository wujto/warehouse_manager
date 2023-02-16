from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Localization, Profile

class LocalizationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.localization = Localization.objects.create(name='Magazyn') #id = 1

    def test_creation_poperly(self):
        self.assertEqual(self.localization.name, 'Magazyn')

    def test_cast_to_string(self):
        self.assertEqual(str(self.localization), 'Magazyn')
    
    def test_modifying(self):
        self.localization = Localization.objects.get(pk=1)
        self.localization.name = 'Localization2'
        self.localization.save()
        obj2 = Localization.objects.get(pk=1)
        self.assertEqual(obj2.name, 'Localization2')

    def test_delete(self):
        self.localization.delete()
        obj2 = Localization.objects.filter(name='Magazyn')
        self.assertEqual(len(obj2), 0)


class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='Test') # id = 1
        cls.user2 = User.objects.create(username='Test2') # id = 2
        cls.localization = Localization.objects.create(name='TestLocalization') #id = 2
        cls.localization2 = Localization.objects.create(
                                                        name='TestLocalization2'
                                                        )
        cls.profile = Profile.objects.create(user=cls.user, 
                                             phone_number='123456789',
                                             localization=cls.localization,
                                             photo='test/test_photo.img')
    
    def test_create(self):
        instance = self.profile
        self.assertIsInstance(instance, Profile)
        self.assertEqual(instance.user.pk, 1)
        self.assertEqual(instance.localization.pk, 2)
        self.assertEqual(instance.phone_number, '123456789')
        self.assertEqual(instance.photo, 'test/test_photo.img')

    def test_modify_and_save(self):
        self.profile.user = self.user2
        self.profile.save()
        self.assertEqual(self.profile.user.pk, self.user2.pk)

        self.profile.localization = self.localization2
        self.profile.save()
        self.assertEqual(self.profile.localization.pk, 3)

        self.profile.phone_number = '123456'
        with self.assertRaises(ValidationError) as e:
            self.profile.save()        
        # print(e.exception.message)

        self.profile.phone_number = '12345adc6'
        with self.assertRaises(ValidationError) as e:
            self.profile.save()
        # print(e.exception.message)

        self.profile.phone_number = '1234567890'
        with self.assertRaises(ValidationError) as e:
            self.profile.save()
        # print(e.exception.message)

    def test_delete_with_user(self):
        self.user.delete()
        with self.assertRaises(ObjectDoesNotExist):
            p = Profile.objects.get(pk=1)