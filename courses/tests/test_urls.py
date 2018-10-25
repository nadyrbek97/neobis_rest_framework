from django.urls import reverse, resolve
from courses.models import *
from django.test import TestCase
from rest_framework.test import APITestCase


class TestCourse(TestCase):

    def test_detail_url(self):
        path = reverse('detail', kwargs={'pk': 1})
        assert resolve(path).view_name == "detail"

    def test_create_course(self):
        course = self.create_course()
        course.contacts.create(type=1, value="0555025045")
        course.branches.create(adress='Bishek', latitude='23.23.23', longitude='343.232')
        self.assertTrue(isinstance(course, Course))


class TestRestFramework(APITestCase):

    pass

