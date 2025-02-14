from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import Restaurant, Menu
from user.models import Vote, Employee


class RestaurantTestCase(TestCase):
    def test_create_restaurant(self):
        restaurant = Restaurant.objects.create(
            name="Ukrainian Feast",
            address="Kyiv, Ukraine",
            cuisine_type="ukrainian"
        )
        self.assertEqual(restaurant.name, "Ukrainian Feast")
        self.assertEqual(restaurant.address, "Kyiv, Ukraine")
        self.assertEqual(restaurant.cuisine_type, "ukrainian")


class MenuTestCase(TestCase):
    def test_create_menu(self):
        restaurant = Restaurant.objects.create(
            name="Italian Delights",
            address="Rome, Italy",
            cuisine_type="italian"
        )
        menu = Menu.objects.create(restaurant=restaurant, date=date.today(), dishes="Pizza, Pasta")

        self.assertEqual(menu.restaurant, restaurant)
        self.assertEqual(menu.dishes, "Pizza, Pasta")
        self.assertEqual(menu.date, date.today())

    def test_upvote_count(self):
        restaurant = Restaurant.objects.create(
            name="Sushi Spot",
            address="Tokyo, Japan",
            cuisine_type="japanese"
        )
        menu = Menu.objects.create(restaurant=restaurant, date=date.today(), dishes="Sushi, Maki")

        user = get_user_model().objects.create_user(email="employee@restaurant.com", password="password123")
        employee_instance = Employee.objects.create(user=user, name="John Doe", position="Dev")

        Vote.objects.create(employee=employee_instance, menu=menu, vote_value=True)

        self.assertEqual(menu.upvote_count, 1)


class VoteTestCase(TestCase):
    def test_create_vote(self):
        restaurant = Restaurant.objects.create(
            name="Mexican Fiesta",
            address="Mexico City, Mexico",
            cuisine_type="mexican"
        )
        menu = Menu.objects.create(restaurant=restaurant, date=date.today(), dishes="Tacos, Burritos")

        user = get_user_model().objects.create_user(email="employee@restaurant.com", password="password123")
        employee_instance = Employee.objects.create(user=user, name="John Doe", position="Dev")

        vote = Vote.objects.create(employee=employee_instance, menu=menu, vote_value=True)

        self.assertEqual(vote.menu, menu)
        self.assertEqual(vote.employee, employee_instance)
        self.assertEqual(vote.vote_value, True)
