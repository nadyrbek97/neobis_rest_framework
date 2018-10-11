from .models import Course , Contact, Branch, Category
from rest_framework import viewsets
from courses.serializers import CourseSerializer,ContactSerializer, BranchSerializer, CategorySerializer




class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class BranchView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer