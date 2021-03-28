from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_required_fields(self):
        form = OrderForm({
            'full_name': '',
            'email': '',
            'phone_number': '',
            'town_or_city': '',
            'street_address1': '',
            'country': '',
            })

        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('phone_number', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertIn('street_address1', form.errors.keys())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_non_required_fields(self):
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@example.com',
            'phone_number': '01234567890',
            'town_or_city': 'test',
            'street_address1': 'test',
            'country': 'GB',
            })

        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
                  'full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2', 'town_or_city',
                  'postcode', 'country', 'county',))
