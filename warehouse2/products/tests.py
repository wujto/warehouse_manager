from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Localization, Profile
from products.models import Product

class ProductTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='Test') # id = 1
        cls.user2 = User.objects.create(username='Test2') # id = 2
        cls.localization = Localization.objects.create(name='TestLocalization') #id = 2
        cls.profile = Profile.objects.create(user=cls.user, 
                                             phone_number='123456789',
                                             localization=cls.localization,
                                             photo='test/test_photo.img')
        cls.profile2 = Profile.objects.create(user=cls.user2, 
                                             phone_number='123456789',
                                             localization=cls.localization,
                                             photo='test/test_photo.img')
        cls.product = Product.objects.create(id_number='0002', name="TestProduct1", description='Test description1')

    def test_add_and_remove_responsible_person(self):
        self.product.responsible_person = self.profile
        self.assertEqual(self.product.responsible_person.pk, self.profile.pk)

        self.product.responsible_person = None
        self.assertEqual(self.product.responsible_person, None)
    
    def test_add_and_delete_transfer_person(self):
        self.product.transfer_person = self.profile
        self.assertEqual(self.product.transfer_person.pk, self.profile.pk)

        self.product.transfer_person = None
        self.assertEqual(self.product.transfer_person, None)

    def test_reject_transfer(self):
        self.product.responsible_person = self.profile
        self.product.transfer_person = self.profile2
        self.product.reject_transfer()
        self.assertEqual(self.product.responsible_person.pk, self.profile.pk)
        self.assertEqual(self.product.transfer_person, None)

    def test_confirm_transfer(self):
        self.product.responsible_person = self.profile
        self.product.transfer_person = self.profile2
        self.product.confirm_transfer()
        self.assertEqual(self.product.responsible_person.pk, self.profile2.pk)
        self.assertEqual(self.product.transfer_person, None)

    def test_set_not_proper_value_in_responsible_person(self):
        with self.assertRaises(ValueError) as e:
            self.product.responsible_person = 100
            self.product.save()
    
    def test_set_not_proper_value_in_transfer_person(self):
        with self.assertRaises(ValueError) as e:
            self.product.transfer_person = 100
            self.product.save()
