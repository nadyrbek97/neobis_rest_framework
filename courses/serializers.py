from rest_framework import serializers
from courses.models import Course,Category,Contact
from .models import *

class CategorySerialezer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    class Meta:
        model = Category

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('contact_type', 'contact_value')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('address', 'latitude', 'longitude')

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    category = CategorySerialezer(read_only=True)
    logo = serializers.CharField(max_length=1000)
    course_contacts = ContactSerializer(read_only=True)
    course_branches = BranchSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ('id','title','description', 'category_name', 'course_contacts', 'course_branches')

    # def create(self, validated_data):
    #     contacts_data = validated_data.pop('contacts')
    #     course = Course.objects.create(**validated_data)
    #     for contact_data in contacts_data:
    #         Contact.objects.create(course=course, **contact_data)
    #     return course
   
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance