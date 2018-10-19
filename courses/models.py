from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, related_name='courses', null=True, on_delete=models.CASCADE)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Branch(models.Model):
    address = models.CharField(max_length=500)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='branches', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'branches'

    def __str__(self):
        return self.address


class Contact(models.Model):
    CONTACT_TYPE = (
        (1, 'PHONE'),
        (2, 'FACEBOOK'),
        (3, 'EMAIL'),
    )
    type = models.IntegerField(choices=CONTACT_TYPE, default=1)
    value = models.CharField(max_length=250)
    course = models.ForeignKey(Course, related_name='contacts', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.value
