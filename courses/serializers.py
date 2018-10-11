from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField( max_length=100)
    class Meta:
        model = Category
        fields = ('category_name', 'category_image')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    contact_type = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ('contact_type', 'contact_value')

    #for getting value of choices
    def get_contact_type(self,obj):
        return obj.get_contact_type_display()

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('address', 'latitude', 'longitude')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    category = CategorySerializer(Category.category_name)
    logo = serializers.CharField(max_length=1000)
    course_contacts = serializers.SerializerMethodField("get_contacts")
    course_branches = serializers.SerializerMethodField("get_branches")
    class Meta:
        model = Course
        fields = ('id','title','description','category','logo', 'course_contacts','course_branches')


    @staticmethod
    def get_contacts(self):
        serializer = ContactSerializer(Contact.objects.all(), many=True)
        return serializer.data

    @staticmethod
    def get_branches(self):
        serializer = BranchSerializer(Branch.objects.all(), many=True)
        return  serializer.data
