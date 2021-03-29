from django.test import TestCase


class TestViews(TestCase):

    def test_get_home_view(self):
        """ These that view is rendered """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
