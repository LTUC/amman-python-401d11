from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class TestHome(SimpleTestCase):
    def test_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        # print(response)
        self.assertEqual(response.status_code, 200)


    def test_home_page_templates(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')