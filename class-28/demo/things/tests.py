from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import Thing
from django.urls import reverse
# Create your tests here.
class Thingtest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='random',email='random@random.com',
            password='random@12345'
        )
        self.thing = Thing.objects.create(
            name = 'test',
            rank=1,
            reviewer = self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.thing),'test')

    def test_detail_view(self):
        url = reverse('thing_detail',args=[self.thing.id])  
        response = self.client.get(url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'things_detail.html')


    def test_create_view(self):
        url = reverse('thing_create')
        data={
            "name": "test_2",
            "reviewer" : self.user.id,
            "rank": 10
        }


        response = self.client.post(path=url,data = data,follow = True)
        self.assertTemplateUsed(response,'things_detail.html')
        self.assertEqual(len(Thing.objects.all()),2)
        self.assertRedirects(response, reverse('thing_detail',args=[2]))




