from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Customer


# Create your tests here.

class ModelsTestCase(TestCase):
    def setUp(self) -> None:
        # Create users
        alice = get_user_model().objects.create_user("alice")
        bob = get_user_model().objects.create_user("bob")
        get_user_model().objects.create_user("charlie")
        get_user_model().objects.create_user("david")

        # Create customers
        Customer.objects.create(name="Alice", sub=True, username=alice)
        Customer.objects.create(name="Bob", sub=False, username=bob)

    def test_users_count(self):
        users = get_user_model().objects
        self.assertEqual(users.count(), 4)

    def test_customers_count(self):
        customers = Customer.objects
        self.assertEqual(customers.count(), 2)

    def test_customer_sub(self):
        alice = get_user_model().objects.get(username="alice")
        bob = get_user_model().objects.get(username="bob")
        self.assertEqual(alice.customer.sub, True)
        self.assertEqual(bob.customer.sub, False)

    def test_one2one(self):
        alice = get_user_model().objects.get(username="alice")
        Alice = Customer.objects.get(name="Alice")
        bob = get_user_model().objects.get(username="bob")
        Bob = Customer.objects.get(name="Bob")
        self.assertEqual(alice.customer, Alice)
        self.assertEqual(bob.customer, Bob)
