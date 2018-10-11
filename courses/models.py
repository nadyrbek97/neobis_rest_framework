from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.CharField(max_length=1000)


class Branch(models.Model):
    address = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Contact(models.Model):
    CONTACT_TYPE = (
        (1, 'PHONE'),
        (2, 'FACEBOOK'),
        (3, 'EMAIL'),
    )
    contact_type = models.IntegerField(choices=CONTACT_TYPE)
    contact_value = models.CharField(max_length=250)

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, related_name='categories',on_delete=models.CASCADE)
    logo = models.CharField(max_length=1000)
    course_contacts = models.ForeignKey(Contact, related_name='contacts', on_delete = models.CASCADE)
    course_branches = models.ForeignKey(Branch, related_name='branches', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

