from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError


class UsersManagersTests(TestCase):

    def test_create_user(self):
        user = get_user_model()
        normal_user = user.objects.create_user(email='normal@user.com', password='foo@@@Foo')
        self.assertEqual(normal_user.email, 'normal@user.com')
        self.assertTrue(normal_user.is_active)
        self.assertFalse(normal_user.is_staff)
        self.assertFalse(normal_user.is_superuser)
        self.assertEqual(normal_user.username, 'normal@user.com')

        with self.assertRaises(ParseError):
            user.objects.create_user()
        with self.assertRaises(ParseError):
            user.objects.create_user(email='')

    def test_create_superuser(self):
        user = get_user_model()
        admin_user = user.objects.create_superuser(email='super@user.com', password='foo@@@fooO')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(ParseError):
            user.objects.create_superuser()
        with self.assertRaises(ParseError):
            user.objects.create_superuser(email='')
