from django.urls import reverse
from django.test import TestCase

from .models import Mineral


# Create your tests here.

class MineralModelTest(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name='Stone'
        )
        self.assertEqual(mineral.name, 'Stone')


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='Granite'
        )

    def test_list_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.mineral.name)

    def test_detail_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.mineral.name)


class MineralFilterTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='Granite'
        )

    def test_category_filter(self):
        resp = self.client.get('/category/sulfate/')
        self.assertEqual(resp.status_code, 200)

    def test_name_filter(self):
        resp = self.client.get('/startswith/g/')
        self.assertEqual(resp.status_code, 200)

    def test_search(self):
        resp = self.client.post('/search/', {'search': 'nyancats'})
        self.assertEqual(resp.status_code, 200)
