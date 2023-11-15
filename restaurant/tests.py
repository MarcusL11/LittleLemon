from django.test import TestCase
from restaurant.models import Booking, Menu

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(first_name="Tester", reservation_date='2023-04-12')
        itemstr = item.get_item()        
        
        self.assertEqual(itemstr, "Tester : 2023-04-12")

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="Tester", price=10 )
        itemstr = item.get_item()        
        
        self.assertEqual(itemstr, "Tester : 10")
