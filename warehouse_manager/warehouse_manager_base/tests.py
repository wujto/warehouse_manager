from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import LocalizationModel, CategoryModel, ProductModel, ProductSetModel

class UserManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        u = User.objects.create_user(email="utest@test.pl",password = 'testpassword', first_name='Test', last_name = 'Test', phone_number = '123456789')
        self.assertEqual(u.email,"utest@test.pl")
        self.assertEqual(u.first_name, 'Test')
        self.assertEqual(u.last_name, 'Test')
        self.assertEqual(u.phone_number, '123456789')
        self.assertTrue(u.is_active)
        self.assertTrue(u.is_staff)
        self.assertFalse(u.is_admin)
        self.assertFalse(u.is_superuser)
        self.assertFalse(u.is_manager)
        try:
            self.assertIsNone(u.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email = '')
        with self.assertRaises(ValueError):
            User.objects.create_user(email = '', password = "foo")

class LocalizationTest(TestCase):
    def test_creation_model(self):
        LocalizationModel(name= "DSK", description= "description")

class CategoryTest(TestCase):
    def test_creation_category(self):
        CategoryModel("Name","")

class ProductSetTest(TestCase):
    def test_create_model(self):
        ProductSetModel("123", "Name","description")

class ProductTest(TestCase):
    def test_create_model(self):
        User = get_user_model()
        u = User.objects.create_user(email="utest@test.pl",password = 'testpassword', first_name='Test', last_name = 'Test', phone_number = '123456789')
        l = LocalizationModel("DSK")
        c = CategoryModel("Tables")
        ps = ProductSetModel("123","set name", 'set description')
        ProductModel("123", "Product", "description",c,l,ps,u)
