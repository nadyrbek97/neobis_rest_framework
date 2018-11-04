from django.urls import reverse, resolve
from courses.models import *
from django.test import TestCase
from rest_framework.test import APITestCase


class TestCourse(TestCase):

    def test_detail_url(self):
        path = reverse('detail', kwargs={'pk': 1})
        assert resolve(path).view_name == "detail"

    def test_create_course(self):
        course = Course.objects.create()
        course.contacts.create(type=1, value="0555025045")
        course.branches.create(address='Bishek', latitude='23.23.23', longitude='343.232')
        self.assertTrue(isinstance(course, Course))

    def test_create_branch(self):
        branch = Branch.objects.create()
        branch.address = 'Osh'
        branch.latitude = '12122.3232'
        branch.longitude = '2332.2323'
        self.assertTrue(isinstance(branch, Branch))

    def test_create_contact(self):
        contact = Contact.objects.create()
        contact.type = 'PHONE'
        contact.value = '0555025045'
        self.assertTrue(isinstance(contact, Contact))


class TestRestFramework(APITestCase):
    pass

