from .models import Category, Course, Branch, Contact
from rest_framework import serializers


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('type', 'value')

    def get_type(self, obj):
        return obj.get_type_display()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True, required=False)
    contacts = ContactSerializer(many=True, required=False)
    category = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = ('title', 'description', 'category', 'logo', 'contacts', 'branches')

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')
        category_data = validated_data.pop('category')

        category_value = category_data['name']

        course = Course.objects.create(**validated_data, category=Category.objects.get(name=category_value))

        for contact in contacts_data:
            contact_type = contacts_data[0]
            type1 = contact_type.pop('type')
            Contact.objects.create(course=course, type=type1, **contact)
        for branch in branches_data:
            Branch.objects.create(course=course, **branch)
        return course
