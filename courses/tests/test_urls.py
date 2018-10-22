from django.urls import reverse, resolve
from courses.models import *

class TestUrls:

    def test_detail_url(self):
        path = reverse('detail', kwargs={'pk': 1})
        assert resolve(path).view_name == "detail"

    def test_create_fnc(self):
        cat = Category.objects.get(pk=1)
        contact = Contact.objects.get(pk=1)
        branch = Branch.objects.get(pk=1)
        course = Course.objects.create(title='judo', description='this is judo', category=cat, logo='judo.img', contact=contact, branch=branch)
        assert course.name == "judo"
