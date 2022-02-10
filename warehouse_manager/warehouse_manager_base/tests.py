from django.test import TestCase
from django.contrib.auth import get_user_model

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