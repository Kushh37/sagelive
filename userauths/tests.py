from django.test import TestCase
from .models import User,ContactUs,Profile

class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create(email='adminadmin@gmail.com', username='testuser', bio='A test bio')

    def test_email_field(self):
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'adminadmin@gmail.com')

    def test_username_field(self):
        user = User.objects.get(email='adminadmin@gmail.com')
        self.assertEqual(user.username, 'testuser')

    def test_bio_field(self):
        user = User.objects.get(email='adminadmin@gmail.com')
        self.assertEqual(user.bio, 'A test bio')

    def test_str_method(self):
        user = User.objects.get(email='adminadmin@gmail.com')
        self.assertEqual(str(user), 'testuser')

class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(email='profiletest@example.com', username='profileuser', bio='Profile bio')

    def test_profile_creation(self):
        self.assertIsNotNone(self.user.profile)

    def test_profile_fields(self):
        profile = self.user.profile
        profile.full_name = "Heet Patel"
        profile.bio = "Bio for Heet"
        profile.phone = "6479200137"
        profile.verified = True
        profile.save()

        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.full_name, "Heet Patel")
        self.assertEqual(updated_profile.bio, "Bio for Heet")
        self.assertEqual(updated_profile.phone, "6479200137")
        self.assertTrue(updated_profile.verified)

    def test_str_method(self):
        profile = self.user
        profile.full_name = None
        profile.bio = "Bio for Heet"
        profile.save()

        self.assertEqual(str(profile), "profileuser")

class ContactUsModelTest(TestCase):

    def setUp(self):
        ContactUs.objects.create(full_name="Heet Patel", email="heet@gmail.com", phone="6479200137", subject="Test Subject", message="Test message")

    def test_fields(self):
        contact = ContactUs.objects.get(email="heet@gmail.com")
        self.assertEqual(contact.full_name, "Heet Patel")
        self.assertEqual(contact.email, "heet@gmail.com")
        self.assertEqual(contact.phone, "6479200137")
        self.assertEqual(contact.subject, "Test Subject")
        self.assertEqual(contact.message, "Test message")

    def test_str_method(self):
        contact = ContactUs.objects.get(email="heet@gmail.com")
        self.assertEqual(str(contact), "Heet Patel")