from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomerProfile, PerformerProfile
from django.contrib.auth.models import User
from .forms import CustomerProfileForm, PerformerProfileForm


class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_customer_profile_creation(self):
        profile = CustomerProfile.objects.create(
            user=self.user,
            name='Test Customer',
            contact_info='test@test.com',
            experience='Some experience'
        )
        self.assertIsInstance(profile, CustomerProfile)
        self.assertEqual(profile.name, 'Test Customer')

    def test_performer_profile_creation(self):
        profile = PerformerProfile.objects.create(
            user=self.user,
            name='Test Performer',
            contact_info='test@test.com',
            experience='Some experience'
        )
        self.assertIsInstance(profile, PerformerProfile)
        self.assertEqual(profile.name, 'Test Performer')

    def tearDown(self):
        self.user.delete()


class ProfileFormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword',
                                             )
        self.customer_profile = CustomerProfile.objects.create(
            user=self.user,
            name='Test Customer',
            contact_info='test@test.com',
            experience='Some experience'
        )
        self.performer_profile = PerformerProfile.objects.create(
            user=self.user,
            name='Test Performer',
            contact_info='test@test.com',
            experience='test experience'
        )

    def test_customer_profile_form_valid(self):
        form_data = {
            # 'user': self.user.pk,
            'name': 'Test Customer',
            'contact_info': 'test@test.com',
            'experience': 'Some experience'
        }
        form = CustomerProfileForm(data=form_data, instance=self.customer_profile)
        self.assertTrue(form.is_valid())

    def test_performer_profile_form_valid(self):
        form_data = {
            # 'user': self.user.pk,
            'name': 'Test performer',
            'contact_info': 'test@test.com',
            'experience': 'Some experience'
        }
        form = PerformerProfileForm(data=form_data, instance=self.performer_profile)
        self.assertTrue(form.is_valid())

    def tearDown(self):
        User.objects.filter(username='testuser').delete()



class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_customer_profile_view(self):
        CustomerProfile.objects.create(
            user=self.user,
            name='Test Customer',
            contact_info='test@test.com',
            experience='Some experience'
        )

        response = self.client.get(reverse('profile:customer_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/customer_profile.html')
        self.assertTrue(CustomerProfile.objects.filter(user=self.user).exists())

    def tearDown(self):
        User.objects.filter(username='testuser').delete()
