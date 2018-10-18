from .models import Category, Course, Branch, Contact
from rest_framework import serializers


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')


class ContactSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Contact
        fields = ('type', 'value')

    def get_type(self, obj):
        return obj.get_type_display()


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    image_path = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Category
        fields = ('name', 'image_path')


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True, required=False)
    contacts = ContactSerializer(many=True, required=False)
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = ('title', 'description', 'category', 'logo', 'contacts', 'branches')

    def create(self, validated_data):
        print(validated_data)
        category_data = validated_data.pop('category')
        print(category_data)
        contacts_data = validated_data.pop('contacts')
        print(contacts_data)
        branches_data = validated_data.pop('branches')
        print(branches_data)
        course = Course.objects.create(**validated_data)
        for contact_data in contacts_data:
            Contact.objects.create(**contact_data, course=course)
        for branch_data in branches_data:
            Branch.objects.create(**branch_data, course=course)
        for cat in category_data:
            c = cat[1]

            Category.objects.create(**cat, course_set=course)
            Category.objects.name(**c)
        return course

