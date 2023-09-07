from django.test import TestCase

# Create your tests here.

class TestDeteiling(TestCase):
    def test_index(self):
        response = self.client.get('/blog_deteiling/')# проверяем на наличие данного приложения. Обязательно ствим "/" перед ссылкой
        self.assertEquals(response.status_code,200)


