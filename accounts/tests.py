from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.
class CustomUserTests(TestCase):
    # test and see if a new user can be created.
    def test_create_user(self):
        User = get_user_model()

        # create_user docs https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user
        # create user creates an actual user with permissions. 
        user = User.objects.create_user(
            username="strikeouts27",
            email="stribling.andrew@gmail.com",
            password="Baseball100!",
        )
        self.assertEqual(user.username, "strikeouts27")
        self.assertEqual(user.email, "stribling.andrew@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # create superuser https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user
    # a different test is required for super users. 

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
