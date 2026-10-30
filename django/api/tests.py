from django.test import TestCase
from django.urls import reverse

from price.models import Price, PriceCategory


class PricesForCalcTests(TestCase):
    def setUp(self):
        self.category = PriceCategory.objects.create(name='Ремонт', description='Работы')
        self.url = reverse('prices_for_calc')

    def create_price(self, **kwargs):
        values = dict(name='Штукатурка', price=100, category=self.category,
                      use_in_calc=True, updated=None)
        values.update(kwargs)
        return Price.objects.create(**values)

    def get_prices(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        return response.json()

    def test_changed_price_and_category_are_visible_on_next_request(self):
        price = self.create_price()
        self.assertEqual(self.get_prices()[0]['price'], 100)
        Price.objects.filter(pk=price.pk).update(price=250)
        PriceCategory.objects.filter(pk=self.category.pk).update(name='Отделка')
        result = self.get_prices()
        self.assertEqual(result[0]['price'], 250)
        self.assertEqual(result[0]['category_name'], 'Отделка')

    def test_price_added_after_empty_response_is_visible(self):
        self.assertEqual(self.get_prices(), [])
        price = self.create_price()
        self.assertEqual([row['id'] for row in self.get_prices()], [price.pk])

    def test_disabled_and_deleted_prices_disappear(self):
        price = self.create_price()
        self.assertEqual(len(self.get_prices()), 1)
        Price.objects.filter(pk=price.pk).update(use_in_calc=False)
        self.assertEqual(self.get_prices(), [])
        Price.objects.filter(pk=price.pk).update(use_in_calc=True)
        self.assertEqual(len(self.get_prices()), 1)
        price.delete()
        self.assertEqual(self.get_prices(), [])
