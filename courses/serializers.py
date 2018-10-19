from .models import Category, Course, Branch, Contact
from rest_framework import serializers


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')


class ContactSerializer(serializers.ModelSerializer):
    #type = serializers.SerializerMethodField()

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
        contacts_data = validated_data.pop('contacts')
        print(contacts_data)
        branches_data = validated_data.pop('branches')
        print(branches_data)
        categ_data = validated_data.pop('category')
        print(categ_data)
        categ_value = categ_data['name']
        print('categ_value: ' + categ_value)


        #categ = Category.courses.filter(name=categ_value)
        #Course.objects.filter(category__name__startswith='John')
        course = Course.objects.create(**validated_data, category=Category.objects.get(name=categ_value))
        print(course)
        for contact in contacts_data:
            contact_type = contacts_data[0]
            print('contact_type: ' + str(contact_type))
            type1 = contact_type.pop('type')
            print('type1: ' + str(type1))
            # type2 = type1[0]
            #print(type2)
            Contact.objects.create(course=course, type=type1, **contact)
        for branch in branches_data:
            Branch.objects.create(course=course, **branch)
        return course
